from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
import time
from Model.updata import up_table
from Model.getdata import get_suser22
# 取消采购申请
# 已测试
class gz_order1(BaseModel):
    id: int
    typess:str
    typess_name:str
    typess_body:str

@app.post('/setorder_typess')
async def up_myorders1(*, Authorization: str = Header(None), data: gz_order1):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        if data.id:
            if get_suser22("x_order",str(data.id))["code"]==0:
                return {"code": 201, "msg": "已建立采购单，无法取消！"}
            else:
     
                field = "send_ctime=null"
                #
                # print(sql)
                # for idx in data.id:
                #     try:
                #
                #     except:
                #         pass
          
                return up_table("x_orders", field, data.id)
        else:
            return {"code": 201, "msg": "访问数据错误"}

    else:
        return {"code": 1001, "msg": msg}

# json 请求数据格式
# {
#      "id":[]
#
#  }