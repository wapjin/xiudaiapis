# 登录
from .conmysql import  c_mysql

def login_get(table,users,passwd):
    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from " + str(table) + " where gonghao = '"+str(users)+"' and passwd  = '"+str(passwd)+"' and ISNULL(dtime)>0"
    print(sql)
    cursor.execute(sql)
    dt = cursor.fetchall()
    print(dt)

    return dt