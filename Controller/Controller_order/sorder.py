
from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.getdata import get_s_order
# 搜索全部未接单的采购单
# 已测试
@app.get('/sorder')
async def search_phasec(*, Authorization: str = Header(None),order_id:str=None,dingding_name:str=None,dingding_bumen:str=None,dingding_xm:str=None,dingding_endtime:str=None,dingding_type:str=None,xiadan_time:str=None,page: int = 1, limit: int = 10):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        # print(fapiao_type)
        return get_s_order("x_orders",order_id,dingding_name,dingding_bumen,dingding_xm,dingding_endtime,dingding_type,xiadan_time,page, limit)


    else:

        return {"code": 1001, "msg": msg}
