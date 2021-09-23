from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.getdata import get_table
# 加载列表
# 已测试
@app.get('/alltable')
async def search_phasec(*, Authorization: str = Header(None), table: str,page: int = 1, limit: int = 10):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        if table:

            return get_table(table, page, limit)


        else:

            return {"code": 201, "msg": "参数错误"}
    else:
        return {"code": 1001, "msg": msg}