
from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.getdata import get_suser
# 用户搜索
# 已测试
@app.get('/suser')
async def search_phasec(*, Authorization: str = Header(None),name:str=None,gonghao:str=None,page: int = 1, limit: int = 10,zhiwei:str=None):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        return get_suser("x_user",gonghao,name,zhiwei,page, limit,None)


    else:

        return {"code": 1001, "msg": msg}