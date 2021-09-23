from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.getdata import get_all_order1,get_all_order2,get_suser2,get_all_order1s,get_all_order2s
# 根据采购申请id拉取采购列表
# 已测试
@app.get('/s_all_order')
async def search_phasec(*, Authorization: str = Header(None),uid:int,gaizhang_type:str=None,fapiao_type:str=None,name:str=None,page: int = 1, limit: int = 10):
    # try:
    # msg = jwts(Authorization)
    # print(msg)
    # if msg == 1:
        data = get_suser2("x_user",str(uid))["data"][0]["ziwei"]
        if data == "管理员":
            
            return get_all_order2(name,page, limit,gaizhang_type,fapiao_type)
        else:
            return get_all_order2s(name,page, limit,uid,gaizhang_type,fapiao_type)



    # else:
    #     return {"code": 1001, "msg": msg}


@app.get('/s_all_orders')
async def search_phasecs(*, Authorization: str = Header(None),s:str,uid:int,name:str=None,page: int = 1, limit: int = 10):
    # try:
    # msg = jwts(Authorization)
    # print(msg)
    # if msg == 1:
        data = get_suser2("x_user",str(uid))["data"][0]["ziwei"]
        if data == "管理员":
        
            return get_all_order1(name,page, limit,s,uid)
        else:

            return get_all_order1s(name, page, limit,uid)



    # else:
    #     return {"code": 1001, "msg": msg}