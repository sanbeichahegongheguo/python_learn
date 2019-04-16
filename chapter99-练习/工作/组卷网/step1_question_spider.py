from urllib.parse import urlencode
import pymysql
import contextlib
import json
import time
from selenium import webdriver
import uuid


# 定义上下文管理器，连接后自动关闭连接
@contextlib.contextmanager
def mysql(host='localhost', port=3333, user='root', password='kuaikang', db='kuaik', charset='utf8'):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=password, db=db, charset=charset)
    conn.autocommit(True)
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield cur
    finally:
        conn.commit()
        cur.close()
        conn.close()


def get_head():
    with open("conf", mode="r", encoding="utf8") as f:
        data = f.read().replace("\n", '').strip()
        return json.loads(data)


def get_chapter_id(book_id):
    with mysql() as cur:
        select_chapter_sql = "SELECT * from chapter WHERE book_id = '{}'".format(book_id)
        cur.execute(select_chapter_sql)
        data = cur.fetchall()
        return [item.get('zj_chapter_id') for item in data]


def get_request_url(categories, page):
    url = "http://www.zujuan.com/question/list?"
    req = {
        "categories": categories,
        "page": page,
        "question_channel_type": "1",  # 题型
        "difficult_index": "",
        "grade_id[]": "0",
        "kid_num": "",
        "exam_type": "",
        "sortField": "time",
        "_": "1521515844117"
    }
    data = []
    url += urlencode(req)
    for i in range(3):
        data.append({"grade_id[]": str(i + 7)})
    url += urlencode(req)
    for d in data:
        url += "&" + urlencode(d)
    return url


driver = webdriver.Chrome()


def parse_data(categories, page):
    url = get_request_url(categories, page)
    driver.get(url)
    time.sleep(2)
    s = driver.find_element_by_tag_name("pre").text
    data = json.loads(s)
    if not data.get('data'):
        return None, None
    return data.get("data")[0].get("questions"), (data.get("total") + 10 - 1) // 10


insert_question = "INSERT INTO t_res_{subject}_question (question_id, context, `type`, difficult,uuid,create_time,update_date) " \
                  "VALUES ('{question_id}', '{context}', '{question_type}', '{difficult}','{question_uuid}',now(),now())"
insert_chap_ques = 'INSERT INTO t_res_{0}_question_chapter (zj_chapter_id, question_id,question_uuid,create_time) VALUES ("{1}", "{2}","{3}",now());'
insert_tag = 'INSERT INTO t_res_{0}_tag_question (tag_url,question_id,question_uuid,tag_id) VALUES ("{1}", "{2}","{3}","{4}");'
insert_item = 'INSERT INTO t_res_{0}_item (p_id,question_uuid,content,create_time,question_option) VALUES ("{1}", "{2}","{3}",now(),"{4}");'
select_question = "select * from t_res_{}_question WHERE  question_id = {}"


def main(subject_key, book_id):
    with mysql() as cur:
        for c_id in get_chapter_id(book_id):
            for page in range(41, 100):
                questions, total_page = parse_data(c_id, page)
                print(book_id, c_id, total_page, page)
                if not total_page or total_page < page: break
                if not questions: break
                for q in questions:
                    if 'base64' in q.get("question_text") or '<table' in q.get("question_text"):
                        continue
                    question_uuid = str(uuid.uuid4()).replace('-', '')
                    if isinstance(q.get("options"), str):
                        continue
                    if isinstance(q.get("options"), list):
                        continue
                    try:
                        cur.execute(
                            insert_chap_ques.format(subject_key, c_id, q.get("question_id"), question_uuid))  # 章节题目关系
                    except Exception:
                        pass
                    if not cur.execute(select_question.format(subject_key, q.get("question_id"))):
                        cur.execute(
                            insert_question.format(
                                subject=subject_key, question_id=q.get("question_id"),
                                context=pymysql.escape_string(q.get("question_text")),
                                question_type="11",
                                difficult=q.get("difficult_index"), question_uuid=question_uuid
                            )
                        )
                        options = q.get("options")
                        for key, val in options.items():  # 选项
                            cur.execute(
                                insert_item.format(
                                    subject_key, str(uuid.uuid4()).replace('-', ''), question_uuid,
                                    pymysql.escape_string(val), key))
                        cur.execute(
                            insert_tag.format(subject_key, q.get("knowledge"), q.get("question_id"), question_uuid,
                                              q.get("question_id")))


if __name__ == '__main__':
    input(">>:")
    sx = ['26823', '26824', '26825']  # '25388', '26821',
    for item in sx:
        main("sx", item)
    driver.quit()
