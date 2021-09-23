from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.getdata import get_tablemyall,get_suser2,get_tablemyall_no
# 我的采购申请单列表
# 已测试
@app.get('/myorder')
async def search_phasec(*, Authorization: str = Header(None),uid:int,page: int = 1, limit: int = 10):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:

        # data = get_suser2("x_user",str(uid))["data"][0]["ziwei"]
        # if data == "管理员":
        #     return get_tablemyall_no("x_orders", page, limit)
        # else:
        return get_tablemyall("x_orders",uid, page, limit)



    else:
        return {"code": 1001, "msg": msg}