
from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.updata import up_table
import time
# 删除供货信息  gonhuo_xinxi
# 已测试
class danwei_del(BaseModel):
    id: int

@app.post('/danwei_del')
async def danwei_dels(*, Authorization: str = Header(None), data: danwei_del):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        if data.id:

            field = "dtime='" + str(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))) + "'"

            return up_table("gonhuo_xinxi",field,data.id)
        else:
            return {"code": 201, "msg": "访问数据错误"}

    else:
        return {"code": 1001, "msg": msg}

