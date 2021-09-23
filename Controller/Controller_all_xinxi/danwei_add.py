
from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.adddata import add_table
from Model.getdata import danwei_s_list1
from Model.updata import up_table
import time
# 添加基础数据 适用表  gonhuo_xinxi
# 已测试
class add_dw(BaseModel):
    gonghuo_danwe: str
    gonghuo_name: str
    gonghuo_itel: str=""
    gonghuo_gtel: str=""
    gonghuo_dizhi: str=""
    gonghuo_cz: str=""
    remark_1: str=""
    remark_2: str=""
    remark_3: str=""
    remark_4: str=""
    remark_5: str=""
    remark_6: str=""

@app.post('/danwei_add')
async def add_danwei(*, Authorization: str = Header(None), data: add_dw):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        if data.gonghuo_danwe and data.gonghuo_name and data.gonghuo_itel:
            dt = danwei_s_list1("gonhuo_xinxi",data.gonghuo_danwe,None,None,None,1, 100)
            if dt["code"]==0:
                 return {"code": 201, "msg": "供应商添加重复！"}
                # field = "dtime=null"

                # up_table("gonhuo_xinxi",dt["data"][0]["id"])
            else:
                field_list = ["gonghuo_danwe","gonghuo_name","gonghuo_itel","gonghuo_gtel","gonghuo_dizhi","gonghuo_cz","remark_1","remark_2","remark_3","remark_4","remark_5","remark_6",
                              "ctime"]
                value_list=[]
                value_list.append(data.gonghuo_danwe)
                value_list.append(data.gonghuo_name)
                value_list.append(data.gonghuo_itel)
                value_list.append(data.gonghuo_gtel)
                value_list.append(data.gonghuo_dizhi)
                value_list.append(data.gonghuo_cz)
                value_list.append(data.remark_1)
                value_list.append(data.remark_2)
                value_list.append(data.remark_3)
                value_list.append(data.remark_4)
                value_list.append(data.remark_5)
                value_list.append(data.remark_6)
                value_list.append(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
                # field = "name='" + str(str(time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))) + "'"
    
                return add_table("gonhuo_xinxi", field_list, value_list)
        else:
            return {"code": 201, "msg": "访问数据错误"}

    else:
        return {"code": 1001, "msg": msg}

