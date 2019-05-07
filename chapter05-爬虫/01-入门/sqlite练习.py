#coding:utf-8

# 各种数据库引擎python顶层均有实现，这里只介绍被包含在标准库中的sqlite(以本地文件的形式存在)
import sqlite3

print("=====================sqlite数据库=====================");

getRC = lambda cur: cur.rowcount if hasattr(cur, 'rowcount') else -1  # 获取游标所指向是数据的行数

try:
    conn = sqlite3.connect('somedatabase.db');  # 连接数据库
    curs=conn.cursor();  # 获取游标
    curs.execute('CREATE TABLE student(id INTEGER PRIMARY KEY,name TEXT)');  # 执行代码,创建表和字段
    curs.execute("INSERT INTO student VALUES(1,'student1')");  # 添加记录
    curs.execute("INSERT INTO student VALUES(?, ?)",[2, 'student2'])  # 添加记录
    num = getRC(curs)  # 获取游标所处理的行数
    conn.commit();  # 每次执行完后都应该保存
except Exception:print("数据表和记录已经添加");
finally:
    curs.execute("UPDATE student SET name='student3' WHERE id=2")  # 更新记录
    curs.execute("SELECT * FROM student");  # 查询记录
    for row in curs.fetchall():
        print(row[0],row[1])
    curs.execute('DELETE FROM student WHERE id=%d' % 1)  # 删除记录
    curs.execute('DROP TABLE student')  # 删除表
    curs.close();  # 关闭游标
    conn.close();
