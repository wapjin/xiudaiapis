from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.updata import up_table
# 更新用户信息
# 已测试
class up_user(BaseModel):
    id: int
    name: str
    users: str
    gonghao: str=""
    passwd: str
    ziwei: str=""
    tel: str=""
@app.post('/upuser')
async def up_user(*, Authorization: str = Header(None), data: up_user):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        if data.id:

            field = "name='" + str(data.name) + "',users='" + str(data.users) + "',gonghao='" + str(data.gonghao) + "',passwd='" +\
                    str(data.passwd) + "',ziwei='" + str(data.ziwei) + "',tel='" + str(data.tel) + "'"
            # sql = "UPDATE x_user SET " + str(field) + " where id='" + str(data.id) + "'"
            #
            # print(sql)
            return up_table("x_user",field,data.id)
        else:
            return {"code": 201, "msg": "访问数据错误"}

    else:
        return {"code": 1001, "msg": msg}

