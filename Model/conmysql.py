import pymysql
from config.mysql_config import mysql
"""
功能：连接数据库


"""
# from config.mysql_config import mysql
origins = []
# 创建 establish
def c_mysql():
    return pymysql.connect(host=str(mysql.host), port=int(mysql.port),user=str(mysql.user),password=str(mysql.passwd), database=str(mysql.bsdata), charset='utf8')
