from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.updata import up_table
from Model.getdata import get_suser,get_suser2
# 更新我的采购单信息
# 已测试
class up_myorder(BaseModel):
    id: int
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
    # uid: int=0


@app.post('/setmyorder')
async def up_myorders(*, Authorization: str = Header(None), data: up_myorder):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        if data.id:
            dd = get_suser2("x_order",str(data.id))
            if dd["code"]==0:
                print(dd)
                name = dd["data"][0]["caigou_name"]
                
                if data.caigou_name !=name:
                    ids =  get_suser("x_user",None,data.caigou_name,None,1, 10)["data"][0]["id"]
                    uid=ids
                    field = "wuliao_lei='" + str(data.wuliao_lei)+"',canpin_name='" + str(data.canpin_name)+"',canpin_guige='" + str(data.canpin_guige)+"',canpin_pinpai='" + str(data.canpin_pinpai)+"',canpin_danwei='" + str(data.canpin_danwei)+"',canpin_shu='" + str(data.canpin_shu)+"',canpin_danjia='" + str(data.canpin_danjia)+"',canpin_shuilv='" + str(data.canpin_shuilv)+"',canpin_zongjia='" + str(data.canpin_zongjia)+"',canpin_endtime='" + str(data.canpin_endtime)+"',gonghuo_name='" + str(data.gonghuo_name)+"',gonghuo_danwe='" + str(data.gonghuo_danwe)+"',gonghuo_itel='" + str(data.gonghuo_itel)+"',gonghuo_gtel='" + str(data.gonghuo_gtel)+"',gonghuo_dizhi='" + str(data.gonghuo_dizhi)+"',gonghuo_cz='" + str(data.gonghuo_cz)+"',hetong_endtime='" + str(data.hetong_endtime)+"',fukan_fangshi='" + str(data.fukan_fangshi)+"',kaipiao_time='" + str(data.kaipiao_time)+"',fapiao_hao='" + str(data.fapiao_hao)+"',yufu_kuan='" + str(data.yufu_kuan)+"',yufu_time='" + str(data.yufu_time)+"',zhongqi_kuan='" + str(data.zhongqi_kuan)+"',zhongqi_time='" + str(data.zhongqi_time)+"',yukuan='" + str(data.yukuan)+"',yukuan_time='" + str(data.yukuan_time)+"',gaizhang_type='" + str(data.gaizhang_type)+"',fapiao_type='" + str(data.fapiao_type)+"',fujian_url='" + str(data.fujian_url)+"',caigou_name='" + str(data.caigou_name)+"',uid='" + str(uid)+"'"
                else:
                    field = "wuliao_lei='" + str(data.wuliao_lei)+"',canpin_name='" + str(data.canpin_name)+"',canpin_guige='" + str(data.canpin_guige)+"',canpin_pinpai='" + str(data.canpin_pinpai)+"',canpin_danwei='" + str(data.canpin_danwei)+"',canpin_shu='" + str(data.canpin_shu)+"',canpin_danjia='" + str(data.canpin_danjia)+"',canpin_shuilv='" + str(data.canpin_shuilv)+"',canpin_zongjia='" + str(data.canpin_zongjia)+"',canpin_endtime='" + str(data.canpin_endtime)+"',gonghuo_name='" + str(data.gonghuo_name)+"',gonghuo_danwe='" + str(data.gonghuo_danwe)+"',gonghuo_itel='" + str(data.gonghuo_itel)+"',gonghuo_gtel='" + str(data.gonghuo_gtel)+"',gonghuo_dizhi='" + str(data.gonghuo_dizhi)+"',gonghuo_cz='" + str(data.gonghuo_cz)+"',hetong_endtime='" + str(data.hetong_endtime)+"',fukan_fangshi='" + str(data.fukan_fangshi)+"',kaipiao_time='" + str(data.kaipiao_time)+"',fapiao_hao='" + str(data.fapiao_hao)+"',yufu_kuan='" + str(data.yufu_kuan)+"',yufu_time='" + str(data.yufu_time)+"',zhongqi_kuan='" + str(data.zhongqi_kuan)+"',zhongqi_time='" + str(data.zhongqi_time)+"',yukuan='" + str(data.yukuan)+"',yukuan_time='" + str(data.yukuan_time)+"',gaizhang_type='" + str(data.gaizhang_type)+"',fapiao_type='" + str(data.fapiao_type)+"',fujian_url='" + str(data.fujian_url)+"',caigou_name='" + str(data.caigou_name)+"'"
            else:
                   field = "wuliao_lei='" + str(data.wuliao_lei)+"',canpin_name='" + str(data.canpin_name)+"',canpin_guige='" + str(data.canpin_guige)+"',canpin_pinpai='" + str(data.canpin_pinpai)+"',canpin_danwei='" + str(data.canpin_danwei)+"',canpin_shu='" + str(data.canpin_shu)+"',canpin_danjia='" + str(data.canpin_danjia)+"',canpin_shuilv='" + str(data.canpin_shuilv)+"',canpin_zongjia='" + str(data.canpin_zongjia)+"',canpin_endtime='" + str(data.canpin_endtime)+"',gonghuo_name='" + str(data.gonghuo_name)+"',gonghuo_danwe='" + str(data.gonghuo_danwe)+"',gonghuo_itel='" + str(data.gonghuo_itel)+"',gonghuo_gtel='" + str(data.gonghuo_gtel)+"',gonghuo_dizhi='" + str(data.gonghuo_dizhi)+"',gonghuo_cz='" + str(data.gonghuo_cz)+"',hetong_endtime='" + str(data.hetong_endtime)+"',fukan_fangshi='" + str(data.fukan_fangshi)+"',kaipiao_time='" + str(data.kaipiao_time)+"',fapiao_hao='" + str(data.fapiao_hao)+"',yufu_kuan='" + str(data.yufu_kuan)+"',yufu_time='" + str(data.yufu_time)+"',zhongqi_kuan='" + str(data.zhongqi_kuan)+"',zhongqi_time='" + str(data.zhongqi_time)+"',yukuan='" + str(data.yukuan)+"',yukuan_time='" + str(data.yukuan_time)+"',gaizhang_type='" + str(data.gaizhang_type)+"',fapiao_type='" + str(data.fapiao_type)+"',fujian_url='" + str(data.fujian_url)+"',caigou_name='" + str(data.caigou_name)+"'"
            
            
            # sql = "UPDATE x_user SET " + str(field) + " where id='" + str(data.id) + "'"
            #
            # print(sql)
            return up_table("x_order",field,data.id)
        else:
            return {"code": 201, "msg": "访问数据错误"}

    else:
        return {"code": 1001, "msg": msg}

# arr=["dingding_name",
# "dingding_bumen",
# "dingding_xm",
# "dingding_endtime",
# "dingding_type",
# "wuliao_lei",
# "xiadan_time",
# "canpin_name",
# "canpin_guige",
# "canpin_pinpai",
# "canpin_danwei",
# "canpin_shu",
# "canpin_danjia",
# "canpin_shuilv",
# "canpin_zongjia",
# "canpin_endtime",
# "gonghuo_name",
# "gonghuo_danwe",
# "gonghuo_itel",
# "gonghuo_gtel",
# "gonghuo_dizhi",
# "gonghuo_cz",
# "hetong_endtime",
# "fukan_fangshi",
# "kaipiao_time",
# "fapiao_hao",
# "yufu_kuan",
# "yufu_time",
# "zhongqi_kuan",
# "zhongqi_time",
# "yukuan",
# "yukuan_time",
# "gaizhang_type",
# "fapiao_type",
# "fujian_url"]
# strs = ""
# for i in arr:
#    strs+= str(i)+'=-" + str(data.'+str(i)+')+"-,'
# print(strs)

# json 请求数据
# {
#      "id":4,
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