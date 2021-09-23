from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.updata import up_table
# # 批量签字
# 已测试
class qz_order(BaseModel):
    id: list




@app.post('/setmyorder_qz')
async def up_myorders(*, Authorization: str = Header(None), data: qz_order):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        if data.id:
            field = "fapiao_type='已签字'"
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