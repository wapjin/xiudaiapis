from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
import time,json,requests
from Model.updata import up_table
from Model.getdata import get_orders

# 接单接口
# 已测试
class ss_order(BaseModel):
    id: int
    uid:int
    caigou_name:str


def dingding_send_msg(caigou_name,ids):
    msg_data = get_orders("x_orders", ids)
    cont = """接单提醒：
项目名："""+msg_data["data"][0]["dingding_xm"]+"""
接单人："""+msg_data["data"][0]["caigou_name"]+"""
指派时间："""+msg_data["data"][0]["cc_time"]+"""
接单时间："""+str(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))+"""
    """
    caigou_name="丁赞成" 
    # caigou_name="茹宏业"
    user_datas = json.loads(requests.get(
        'http://172.16.1.19:8024/dingding/getUserPage?page=1&limit=10&data={"name":"' + caigou_name + '"}').text)
    print(user_datas)
    if user_datas["count"]>0:

        url = "http://172.16.1.19:8024/dingding/sendMessage?userIdList=" + str(user_datas["data"][0]["userId"]) + "&content=" + cont
        # url="http://192.168.253.3:8021/dingding/sendMessage?userIdList="+str(uid)+"&content="+cont
        return json.loads(requests.post(url).text)
    else:
        return {"errcode":1,"msg":"发送失败"}
@app.post('/setorder')
async def up_myorders(*, Authorization: str = Header(None), data: ss_order):
    # try:
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        if data.id:
            # field = "uid='" + str(data.uid)+"',caigou_name='" + str(data.caigou_name)+"'"
            # #   str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            # # print(sql)
            # return up_table("x_orders",field,data.id)
            field = "send_ctime='" + str(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))+"'"
            dingding_send_msg(data.caigou_name,data.id)
            return up_table("x_orders",field,data.id)
        else:
            return {"code": 201, "msg": "访问数据错误"}

    else:
        return {"code": 1001, "msg": msg}

# json 请求数据格式
# {
#      "caigou_name":"刘进",
#      "uid":2,
#      "id":3
#
#  }