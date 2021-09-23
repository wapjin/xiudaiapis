
from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.getdata import all_s_list
# 搜索基础数据  适用表  caigou_type  chanpin_danwei  wuliao_lei xm_name
# 已测试
@app.get('/all_s_list')
async def all_s_lists(*, Authorization: str = Header(None),name:str=None,table:str,page: int = 1, limit: int = 10):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        # print(fapiao_type)
        return all_s_list(table,name,page, limit)

    else:

        return {"code": 1001, "msg": msg}
