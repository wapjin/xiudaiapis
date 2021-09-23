
from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.updata import up_table
from Model.getdata import all_s_list1,all_s_list
import time
# 更新基础数据  适用表  caigou_type  chanpin_danwei  wuliao_lei xm_name
# 已测试
class up_all(BaseModel):
    id: int
    table: str
    name: str

@app.post('/all_up_list')
async def up_alls(*, Authorization: str = Header(None), data: up_all):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        if data.id and data.table and data.name:
            dt1 = all_s_list1(data.table,str(data.name),1, 100)
            if dt1["code"]==0:
                return {"code": 201, "msg": "名称重复！"}
            else:
                field = "name='" + str(data.name) + "'"
    
                return up_table(data.table,field,data.id)
        else:
            return {"code": 201, "msg": "访问数据错误"}

    else:
        return {"code": 1001, "msg": msg}

