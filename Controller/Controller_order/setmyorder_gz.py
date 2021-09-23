from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.updata import up_table
# 批量盖章
# 已测试
class gz_order(BaseModel):
    id: list




@app.post('/setmyorder_gz')
async def up_myorders(*, Authorization: str = Header(None), data: gz_order):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        if data.id:
            field = "gaizhang_type='已审批'"
            #
            # print(sql)
            for id in data.id:
                try:
                    up_table("x_order", field, id)
                except:
                    pass
            return {"code": 0, "msg": "修改成功！"}
        else:
            return {"code": 201, "msg": "访问数据错误"}

    else:
        return {"code": 1001, "msg": msg}

# json 请求数据格式
# {
#      "id":[]
#
#  }