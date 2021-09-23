from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.adddata import add_table
from Model.getdata import get_orderid,get_suser2,get_suser

import time
# 添加采购身亲的采购单信息
# 已测试
class news_myorder(BaseModel):
    orderid:int
    wuliao_lei: str=""
    canpin_name: str=""
    canpin_guige: str=""
    canpin_pinpai: str=""
    canpin_danwei: str=""
    canpin_shu: str=""
    canpin_danjia: str=""
    canpin_shuilv: str=""
    canpin_zongjia: str=""
    canpin_endtime: str=""
    caigou_name: str=""
    gonghuo_name: str=""
    gonghuo_danwe: str=""
    gonghuo_itel: str=""
    gonghuo_gtel: str=""
    gonghuo_dizhi: str=""
    gonghuo_cz: str=""
    hetong_endtime: str=""
    fukan_fangshi: str=""
    kaipiao_time: str=""
    fapiao_hao: str=""
    yufu_kuan: str=""
    yufu_time: str=""
    zhongqi_kuan: str=""
    zhongqi_time: str=""
    yukuan: str=""
    yukuan_time: str=""
    gaizhang_type: str=""
    fapiao_type: str=""
    fujian_url: str=""
    uid:int=None



@app.post('/add_new_order')
async def up_myorders(*, Authorization: str = Header(None), data: news_myorder):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        if data.orderid:

            field_list=["order_id",
            "wuliao_lei",
            "canpin_name",
            "canpin_guige",
            "canpin_pinpai",
            "canpin_danwei",
            "canpin_shu",
            "canpin_danjia",
            "canpin_shuilv",
            "canpin_zongjia",
            "canpin_endtime",
            "gonghuo_name",
            "gonghuo_danwe",
            "gonghuo_itel",
            "gonghuo_gtel",
            "gonghuo_dizhi",
            "gonghuo_cz",
            "hetong_endtime",
            "fukan_fangshi",
            "kaipiao_time",
            "fapiao_hao",
            "yufu_kuan",
            "yufu_time",
            "zhongqi_kuan",
            "zhongqi_time",
            "yukuan",
            "yukuan_time",
            "gaizhang_type",
            "fapiao_type",
            "fujian_url","orderid"]
            # field_list = ["name"]

            value_list = []
            for ids in range(1,1000):
                isds = '%03d' % ids
                order_id="XY"+str(time.strftime("%Y%m%d", time.localtime()))+isds
                print(order_id)
                datas = get_orderid("x_order",str(order_id),1,10)
                print(datas)
                if datas["code"]!=0:
                    break


            value_list.append(order_id)

            # value_list.append(data.uid)

            value_list.append(data.wuliao_lei)

            value_list.append(data.canpin_name)
            value_list.append(data.canpin_guige)
            value_list.append(data.canpin_pinpai)
            value_list.append(data.canpin_danwei)
            value_list.append(data.canpin_shu)
            value_list.append(data.canpin_danjia)
            value_list.append(data.canpin_shuilv)
            value_list.append(data.canpin_zongjia)
            value_list.append(data.canpin_endtime)
            value_list.append(data.gonghuo_name)
            value_list.append(data.gonghuo_danwe)
            value_list.append(data.gonghuo_itel)
            value_list.append(data.gonghuo_gtel)
            value_list.append(data.gonghuo_dizhi)
            value_list.append(data.gonghuo_cz)
            value_list.append(data.hetong_endtime)
            value_list.append(data.fukan_fangshi)
            value_list.append(data.kaipiao_time)
            value_list.append(data.fapiao_hao)
            value_list.append(data.yufu_kuan)
            value_list.append(data.yufu_time)
            value_list.append(data.zhongqi_kuan)
            value_list.append(data.zhongqi_time)
            value_list.append(data.yukuan)
            value_list.append(data.yukuan_time)
            value_list.append(data.gaizhang_type)
            value_list.append(data.fapiao_type)
            value_list.append(data.fujian_url)
            value_list.append(data.orderid)
            if data.caigou_name:
                 ids =  get_suser("x_user",None,data.caigou_name,None,1, 10)["data"][0]["id"]
                 field_list.append("uid")
                 value_list.append(ids)
                
                #  data = get_suser2("x_user",str(data.uid))["data"][0]["name"]
                 field_list.append("caigou_name")
                 value_list.append(data.caigou_name)
            else:
                field_list.append("uid")
                value_list.append(data.uid)
                
                data = get_suser2("x_user",str(data.uid))["data"][0]["name"]
                field_list.append("caigou_name")
                value_list.append(data)

            # value_list.append(str(time.strftime("%Y-%m-%d %H.%M.%S", time.localtime())))

            return add_table("x_order", field_list, value_list)

        else:
            return {"code": 201, "msg": "访问数据错误"}

    else:
        return {"code": 1001, "msg": msg}

# field_list=["caigou_name","uid","dingding_name",
#             "dingding_bumen",
#             "dingding_xm",
#             "dingding_endtime",
#             "dingding_type",
#             "wuliao_lei",
#             "xiadan_time",
#             "canpin_name",
#             "canpin_guige",
#             "canpin_pinpai",
#             "canpin_danwei",
#             "canpin_shu",
#             "canpin_danjia",
#             "canpin_shuilv",
#             "canpin_zongjia",
#             "canpin_endtime",
#             "gonghuo_name",
#             "gonghuo_danwe",
#             "gonghuo_itel",
#             "gonghuo_gtel",
#             "gonghuo_dizhi",
#             "gonghuo_cz",
#             "hetong_endtime",
#             "fukan_fangshi",
#             "kaipiao_time",
#             "fapiao_hao",
#             "yufu_kuan",
#             "yufu_time",
#             "zhongqi_kuan",
#             "zhongqi_time",
#             "yukuan",
#             "yukuan_time",
#             "gaizhang_type",
#             "fapiao_type",
#             "fujian_url"]
# strs = ""
# for i in field_list:
#    print('value_list.append(data.'+str(i)+')')
#    strs+='"'+str(i)+'":"",'
# print(strs)
# for ids in range(1,1000):
#     print('%03d' % ids)

# json 请求数据
# {
#      "caigou_name":"1",
#      "uid":4,
#      "dingding_name":"1",
#      "dingding_bumen":"1",
#      "dingding_xm":"1",
#      "dingding_endtime":"1",
#      "dingding_type":"1",
#      "wuliao_lei":"1",
#      "xiadan_time":"1",
#      "canpin_name":"1",
#      "canpin_guige":"1",
#      "canpin_pinpai":"1",
#      "canpin_danwei":"1",
#      "canpin_shu":"1",
#      "canpin_danjia":"1",
#      "canpin_shuilv":"1",
#      "canpin_zongjia":"1",
#      "canpin_endtime":"1",
#      "gonghuo_name":"1",
#      "gonghuo_danwe":"1",
#      "gonghuo_itel":"1",
#      "gonghuo_gtel":"1",
#      "gonghuo_dizhi":"1",
#      "gonghuo_cz":"1",
#      "hetong_endtime":"1",
#      "fukan_fangshi":"1",
#      "kaipiao_time":"1",
#      "fapiao_hao":"1",
#      "yufu_kuan":"1",
#      "yufu_time":"1",
#      "zhongqi_kuan":"1",
#      "zhongqi_time":"1",
#      "yukuan":"1",
#      "yukuan_time":"1",
#      "gaizhang_type":"1",
#      "fapiao_type":"1",
#      "fujian_url":"1"
#
#  }