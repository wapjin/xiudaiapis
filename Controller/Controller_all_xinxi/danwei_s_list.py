
from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.getdata import danwei_s_list
# 搜索供应商信息
# 已测试
@app.get('/danwei_s_list')
async def all_s_lists(*, Authorization: str = Header(None),gonghuo_danwe:str=None,gonghuo_name:str=None,gonghuo_itel:str=None,gonghuo_dizhi:str=None,page: int = 1, limit: int = 10):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        # print(fapiao_type)
        return danwei_s_list("gonhuo_xinxi",gonghuo_danwe,gonghuo_name,gonghuo_itel,gonghuo_dizhi,page, limit)

    else:

        return {"code": 1001, "msg": msg}
