
from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.adddata import add_table
from Model.getdata import all_s_list1,all_s_list
from Model.updata import up_table
import time
# 添加基础数据 适用表  caigou_type  chanpin_danwei  wuliao_lei xm_name
# 已测试
class add_all(BaseModel):
    name: str
    table: str

@app.post('/all_add_list')
async def add_alls(*, Authorization: str = Header(None), data: add_all):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        if data.name and data.table:
            
            dt = all_s_list1(data.table,str(data.name),1, 100)
            print(dt)
            if dt["code"]==0:
                field = "dtime=null"
                dd= up_table(data.table,field,dt["data"][0]["id"])
                if dd["code"]==0:
                     dd["msg"]="提交的名称重复，故已恢复！"
                     dd["code"]=201
                else:
                     dd["msg"]="添加失败！"
                return dd
                
            else:
                field_list = ["name","ctime"]
                value_list=[]
                value_list.append(data.name)
                value_list.append(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
                # field = "name='" + str(str(time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))) + "'"
                dd = add_table(data.table, field_list, value_list)
                if dd["code"]==0:
                     dd["msg"]="添加成功"
                else:
                     dd["msg"]="添加失败！"
                return dd
        else:
            return {"code": 201, "msg": "访问数据错误"}

    else:
        return {"code": 1001, "msg": msg}

