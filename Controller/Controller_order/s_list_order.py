from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.getdata import get_tablemyalls
# 根据采购申请id拉取采购列表
# 已测试
@app.get('/s_list_order')
async def search_phasec(*, Authorization: str = Header(None),id:int,page: int = 1, limit: int = 10):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:


        return get_tablemyalls("x_order",id, page, limit)



    else:
        return {"code": 1001, "msg": msg}