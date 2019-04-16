import pymysql, requests, re, time, threading
from urllib.parse import urlencode
from bs4 import BeautifulSoup


def get_db():
    # 打开数据库连接
    try:
        db = pymysql.connect(
            host="localhost", user="root",
            password="kuaikang", db="lezhi", port=3333,
            charset="utf8"
        )
        return db
    except Exception as e:
        print(e)


def insert_grade():
    db = get_db()
    cur = db.cursor()
    sql_grade = "INSERT INTO grade (`grade_id`, `grade_name`) VALUES ('%s', '%s');"
    dic = {'G04': '一年级', 'G05': '二年级', 'G06': '三年级', 'G07': '四年级', 'G08': '五年级', 'G09': '六年级', 'G10': '七年级',
           'G11': '八年级', 'G12': '九年级', 'G13': '高一', 'G14': '高二', 'G15': '高三'}
    for key, val in dic.items():
        cur.execute(sql_grade % (key, val))
        db.commit()
    cur.close()
    db.close()


def insert_book():
    sql = "INSERT INTO book (`book_id`, `book_name`, `course_id`, `version_id`, `grade_id`) VALUES ('%s', '%s', '%s', '%s', '%s');"
    db = get_db()
    cur = db.cursor()
    f = open("book.txt", mode="r", encoding="utf8")
    for line in f.readlines():
        line = line.split(",")
        cur.execute(sql % (line[3], line[4], line[1], line[2], line[0]))
        db.commit()
    f.close()
    cur.close()
    db.close()


def insert_version():
    db = get_db()
    cur = db.cursor()
    p_id = 200000
    sql = "INSERT INTO version (`p_id`, `grade_id`, `course_id`, `version_id`, `version_name`) " \
          "VALUES ('%s', '%s', '%s', '%s', '%s');"
    f = open("version.txt", mode="r", encoding="utf8")
    for line in f.readlines():
        line = line.split(",")
        cur.execute(sql % (p_id, line[0], line[1], line[2], line[3].strip()))
        p_id += 1
        db.commit()
    f.close()
    cur.close()
    db.close()


def insert_chapter():
    db = get_db()
    cur = db.cursor()
    sql = "select book_id,course_id,version_id,grade_id from book WHERE  book_id in ('3736', 'ff8080814467cea80144681413c7027c', 'ff8080814467cea8014468172fd1029c','ff8080814467cea80144681f50c70300', 'ff8080814467cea80144683d582603e6'," \
          "'ff8080814467cea8014468404ea00407', '3528', '3607', '3739', 'ff8080814467cea80144680c079d0251','ff8080814467cea801446826ceb1034a', 'ff8080814467cea80144682d1f9a0375')"
    cur.execute(sql)
    books = cur.fetchall()
    insert_chapter_sql = "INSERT INTO chapter (`chapter_id`, `chapter_name`, `parent_id`, `book_id`, `lesson_type`, `no`) " \
                         "VALUES ('%s', '%s', '%s', '%s', '%s', '%s');"
    for book in books:
        data = {

            "gradeId": book[3],
            "courseId": book[1],
            "versionId": book[2]
        }
        resp = requests.post(
            "http://www.jiaoxueyun.cn/resources-more-inter!getTrees.do?&volumeId=%s&" % book[0] + urlencode(data)
        )
        if "CourseListId" in resp.text:
            for j in resp.json():
                cur.execute(
                    insert_chapter_sql % (j.get("CourseListId"),
                                          pymysql.escape_string(j.get("CourseListName")),
                                          j.get("ParentId"), book[0],
                                          j.get("LessonType"),
                                          j.get("SqNo")))
        db.commit()
    cur.close()
    db.close()


def insert_resource(book_id, res_type):
    db = get_db()
    cur = db.cursor()
    sql = "SELECT b.grade_id,b.version_id,b.course_id,c.chapter_id,b.book_id from chapter c " \
          "LEFT JOIN book b on c.book_id = b.book_id WHERE c.book_id='%s'" % book_id
    insert_resource = "INSERT INTO resource (`resource_id`, `resource_name`, `book_id`, `chapter_id`,`type`) " \
                      "VALUES ('%s', '%s', '%s', '%s', '%s');"
    resource_select = "SELECT * FROM resource WHERE resource_id = '%s' and chapter_id = '%s';"
    url = "http://www.jiaoxueyun.cn/resources-more!getTeachingResource.do?"
    pattern = re.compile(".*?resource_id=(.*?)&.*?", re.S)
    cur.execute(sql)
    chapters = cur.fetchall()
    for chapter in chapters:
        data = {
            "type": "T01,",
            "gradeId": chapter[0],
            "versionId": chapter[1],
            "courseId": chapter[2],
            "nodeId": chapter[3],
            "extension_name": res_type
        }
        try:
            resp = requests.get(url=url + urlencode(data), timeout=10)
        except Exception:
            continue
        soup = BeautifulSoup(resp.text, "lxml")
        tds = soup.find_all(attrs={"style": "font-weight: bold;cursor: pointer;"})
        if not tds: continue
        for td in tds:
            resource_id = re.findall(pattern, td["onclick"])[0]
            try:
                cur.execute(insert_resource % (
                    resource_id, pymysql.escape_string(td["title"]), chapter[4], chapter[3], res_type))
            except:
                print('已存在', resource_id, chapter[3])
        db.commit()
        time.sleep(0.2)
    cur.close()
    db.close()


def main(book_id, res_types):
    for kind in res_types:
        insert_resource(book_id, kind)


if __name__ == '__main__':
    tp = ['DOC', 'DOCX', 'PPT', 'PPTX', 'JPG', 'MP4']
    book_ids = ['3736', 'ff8080814467cea80144681413c7027c', 'ff8080814467cea8014468172fd1029c',
                'ff8080814467cea80144681f50c70300', 'ff8080814467cea80144683d582603e6',
                'ff8080814467cea8014468404ea00407', '3528', '3607', '3739', 'ff8080814467cea80144680c079d0251',
                'ff8080814467cea801446826ceb1034a', 'ff8080814467cea80144682d1f9a0375']
    for ids in book_ids:
        t = threading.Thread(target=main, args=(ids, tp,))
        t.start()
