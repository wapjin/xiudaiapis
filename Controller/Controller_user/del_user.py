
from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.updata import up_table
import time
# 删除用户
# 已测试
class del_user(BaseModel):
    id: int

@app.post('/del_user')
async def up_user(*, Authorization: str = Header(None), data: del_user):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        if data.id:

            field = "dtime='" + str(str(time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))) + "'"

            return up_table("x_user",field,data.id)
        else:
            return {"code": 201, "msg": "访问数据错误"}

    else:
        return {"code": 1001, "msg": msg}

