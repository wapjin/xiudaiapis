
from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.updata import up_table
import time
# 删除基础数据 适用所有表格  caigou_type  chanpin_danwei  wuliao_lei xm_name gonhuo_xinxi
# 已测试
class del_all(BaseModel):
    id: int
    table: str

@app.post('/all_del_list')
async def del_alls(*, Authorization: str = Header(None), data: del_all):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        if data.id and data.table:

            field = "dtime='" + str(str(time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))) + "'"

            return up_table(data.table,field,data.id)
        else:
            return {"code": 201, "msg": "访问数据错误"}

    else:
        return {"code": 1001, "msg": msg}

