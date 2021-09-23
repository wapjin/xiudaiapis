from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.adddata import add_table
from Model.getdata import get_dels
from Model.updata import up_table
# 用户新增
# 用户新增
# 已测试
class add_user(BaseModel):
    name: str
    users: str
    gonghao: str=""
    passwd: str="123456"
    ziwei: str=""
    tel: str=""

@app.post('/add_user')
async def add_userc(*, Authorization: str = Header(None), data: add_user):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        
        data_user= get_dels("x_user", " gonghao='"+data.gonghao+"' and ISNULL(dtime)<=0")
        if data_user["code"]==0:
            field = "name='" + str(data.name) + "',users='" + str(data.users) + "',gonghao='" + str(data.gonghao) + "',passwd='" +\
                    str(data.passwd) + "',ziwei='" + str(data.ziwei) + "',tel='" + str(data.tel) + "',dtime=null"

            return up_table("x_user",field,data_user["data"][0]["id"])
        else:
            
            field_list = ["name", "users", "gonghao", "passwd", "ziwei", "tel"]
    
            value_list = []
            value_list.append(data.name)
            value_list.append(data.users)
            value_list.append(data.gonghao)
            value_list.append(data.passwd)
            value_list.append(data.ziwei)
            value_list.append(data.tel)
    
            return add_table("x_user", field_list, value_list)


    else:
        return {"code": 1001, "msg": msg}

