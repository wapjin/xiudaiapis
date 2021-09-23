from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.getdata import get_tablemyallsd,get_tablemyallsd2,get_suser2
# 我的采购单列表
# 已测试  /myorders
@app.get('/myorders')
async def search_phasec(*, Authorization: str = Header(None),uid:int,page: int = 1, limit: int = 10):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:

        data = get_suser2("x_user",str(uid))["data"][0]["ziwei"]
        if data == "管理员":
            return get_tablemyallsd2("x_order", page, limit)
        else:
            return get_tablemyallsd("x_order",uid, page, limit)
        
        # return get_tablemyall("x_order",uid, page, limit)



    else:
        return {"code": 1001, "msg": msg}