
# 添加信息
from .conmysql import  c_mysql
def add_table(table,field_list,value_list):
    try:

        db = c_mysql()
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        if len(field_list)>1:
            sql = "INSERT INTO "+str(table)+ " "+str(tuple(field_list)).replace("'","")+" VALUES "+str(tuple(value_list))
        else:
            sql = "INSERT INTO "+str(table)+ " "+str(tuple(field_list)).replace("'","").replace(",","")+" VALUES "+str(tuple(value_list)).replace(",","")


        print(sql)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return {'code': 0, 'msg': "添加成功"}
    except BaseException as e:
        print('\033[31m'+str(e)+'\033[0m')
        return {'code': 201, 'msg': "添加失败"}