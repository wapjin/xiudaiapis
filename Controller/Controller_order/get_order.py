from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.getdata import get_tableall
# 获取接单列表
# 已测试
@app.get('/get_order')
async def search_phasec(*, Authorization: str = Header(None),page: int = 1, limit: int = 10,uid:int):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:


        return get_tableall("x_orders", page, limit,uid)



    else:
        return {"code": 1001, "msg": msg}