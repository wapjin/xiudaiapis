
from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.getdata import get_s_myorder
# 搜索我的采购申请单
# 已测试
@app.get('/smyorder')
async def search_phasec(*, Authorization: str = Header(None),uid:int,order_id:str=None,dingding_name:str=None,dingding_bumen:str=None,dingding_xm:str=None,dingding_endtime:str=None,dingding_type:str=None,fapiao_type:str=None,gaizhang_type:str=None,xiadan_time:str=None,page: int = 1, limit: int = 10):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        print(fapiao_type)
        return get_s_myorder("x_orders",uid,order_id,dingding_name,dingding_bumen,dingding_xm,dingding_endtime,dingding_type,xiadan_time,gaizhang_type,fapiao_type,page, limit)


    else:

        return {"code": 1001, "msg": msg}
