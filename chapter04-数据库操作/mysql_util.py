import pymysql
import contextlib


@contextlib.contextmanager
def mysql(db, host='123.206.227.74', port=3306, user='root', password='exue2017', charset='utf8'):
    """第一个参数是db(必传),连接的是123.206.227.74,查询返回的是字典数组"""
    conn = pymysql.connect(host=host, port=port, user=user, passwd=password, db=db, charset=charset)
    conn.autocommit(True)
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield cur
    finally:
        cur.close()
        conn.close()


def get_db(db):
    # 打开数据库连接
    db = pymysql.connect(
        host="192.168.121.159", user="dept_jz",
        password="nimo_PL<", db=db, port=42578,
        charset="utf8"
    )
    return db