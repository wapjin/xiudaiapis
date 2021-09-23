from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.updata import up_table
from Model.getdata import danwei_s_list1
import time
# 更新供应商数据  适用表  gonhuo_xinxi
# 已测试
class danwei_up(BaseModel):
    id: int
    gonghuo_danwe: str
    gonghuo_name: str
    gonghuo_itel: str=""
    gonghuo_gtel: str = ""
    gonghuo_dizhi: str = ""
    gonghuo_cz: str = ""
    remark_1: str = ""
    remark_2: str = ""
    remark_3: str = ""
    remark_4: str = ""
    remark_5: str = ""
    remark_6: str = ""

@app.post('/danwei_up')
async def danwei_ups(*, Authorization: str = Header(None), data: danwei_up):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        if data.id:
            dt1 = danwei_s_list1("gonhuo_xinxi",data.gonghuo_danwe,None,None,None,1, 100)
            if dt1["code"]==0:
                if data.id == dt1["data"][0]["id"]:
                    field = "gonghuo_danwe='" + str(data.gonghuo_danwe) + "',gonghuo_name='" + str(data.gonghuo_name) +\
                        "',gonghuo_itel='" + str(data.gonghuo_itel) + "',gonghuo_gtel='" + str(data.gonghuo_gtel) +\
                        "',gonghuo_dizhi='" + str(data.gonghuo_dizhi) + "',gonghuo_cz='" + str(data.gonghuo_cz) + "',remark_1='" + str(data.remark_1) + "',remark_2='" + str(data.remark_2) + "',remark_3='" + str(data.remark_3) + "',remark_4='" + str(data.remark_4) + "',remark_5='" + str(data.remark_5) + "',remark_6='" + str(data.remark_6) + "'"
    
                    return up_table("gonhuo_xinxi",field,data.id)
                    pass
                else:
                    return {"code": 201, "msg": "请不要重复添加！"}
            else:
                field = "gonghuo_danwe='" + str(data.gonghuo_danwe) + "',gonghuo_name='" + str(data.gonghuo_name) +\
                        "',gonghuo_itel='" + str(data.gonghuo_itel) + "',gonghuo_gtel='" + str(data.gonghuo_gtel) +\
                        "',gonghuo_dizhi='" + str(data.gonghuo_dizhi) + "',gonghuo_cz='" + str(data.gonghuo_cz) + "',remark_1='" + str(data.remark_1) + "',remark_2='" + str(data.remark_2) + "',remark_3='" + str(data.remark_3) + "',remark_4='" + str(data.remark_4) + "',remark_5='" + str(data.remark_5) + "',remark_6='" + str(data.remark_6) + "'"
    
                return up_table("gonhuo_xinxi",field,data.id)
        else:
            return {"code": 201, "msg": "访问数据错误"}

    else:
        return {"code": 1001, "msg": msg}

