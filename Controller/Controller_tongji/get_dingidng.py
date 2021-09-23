# 获取钉钉的表单信息
from runs import app
from fastapi import Header
from pydantic import BaseModel
from ..jwts import jwts
import requests, json, time, os
# 获取新跃的token
from Model.adddata import add_table
from Model.getdata import get_suser
from Model.getdata import get_xiadan
from qiniu import Auth, put_file, etag
import qiniu.config
import time

def ups(p, name):
    # 需要填写你的 Access Key 和 Secret Key
    accessKey = "M5v-NC-OHhgyv0O-ORD2uEvwjsT1VuOiYbQUvery"
    secretKey = "vIsElpWC6G0fw3gX1shFm0f1L6GMPvTeTw5Wfz-O"

    # 构建鉴权对象
    q = Auth(accessKey, secretKey)
    # 要上传的空间
    bucket = "xh-smart-park"
    # 上传后保存的文件名
    key = name
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket, key, 3600)
    # 要上传文件的本地路径
    localfile = p
    ret, info = put_file(token, key, localfile, version='v2')
    print(info)
    if ret['hash']:
        return True
    else:
        return False
    # assert ret['key'] == key
    # assert  == etag(localfile)


def get_files_json(token, listcode, name,listcode1):
    # exit()
    print(listcode)
    print(type(listcode))
    # print(listcode)
    # print(listcode[len(listcode)-1])
    for p in range(len(listcode)):
        if str(listcode[p]["fileName"]) == str(name):
            file_id = listcode[p]["fileId"]



    print(file_id)
    print(listcode1)
    # print(requests.get("https://oapi.dingtalk.com/topapi/processinstance/get?access_token="+token+"&process_instance_id="+str(lsits[len(lsits)-1])).text)
    data1 = {
        'request': '{"process_instance_id":"' + listcode1 + '","file_id":"' + file_id + '"}'
    }

    # print(data1)
    dt = json.loads(requests.post("https://oapi.dingtalk.com/topapi/processinstance/file/url/get?access_token=" + token,
                                  data=data1).text)
    print(dt)
    data_url = {
        "img_url": dt["result"]["download_uri"],
        "name": name
    }
    # requests.get()
    pas = os.getcwd().split("\Controller\Controller_tongji")
    print(pas)
    r = requests.get(dt["result"]["download_uri"])
    with open(os.path.join(pas[0], "files", name), "wb+") as code:
        code.write(r.content)

    if ups(os.path.join(pas[0], "files", name), name):
        data = {"name":name,"url": "http://smart.park.xinhai.com/" + name}
    else:
        data = ""
    return data

def get_token():
    appkey = "dinga0btkunvnsp95x9z"
    # appkey="dingzt2yhhbuntieojpu"
    appsecret = "W4m4PMv02gb2rJzWOegp0Yx5UGKl-NiIyS5inusgrJ_05mwmKjta8hypuUwaFpc2"
    # appsecret="qKH8e-Ka61gQr2B27OMjz3d9H7ajR7cmtH9XkRfUzDvkCavsAZa-N2nunS86beV-"
    return json.loads(
        requests.get("https://oapi.dingtalk.com/gettoken?appkey=" + str(appkey) + "&appsecret=" + str(appsecret)).text)[
        "access_token"]


def get_idlist(start, end, access_token):
    dt = str(start) + ' 00:00:00'
    dts = str(end) + ' 23:00:00'
    ts = int(time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S")))
    tss = int(time.mktime(time.strptime(dts, "%Y-%m-%d %H:%M:%S")))
    # access_token=get_token()
    # access_token="0e90cb734b6d397fba82d19577e8c442"
    # process_code="PROC-D449F2F2-CA8B-415D-BFA7-5F49A6F66BBF"
    # process_code="PROC-E3C89E28-5871-4181-AA9C-907EACCC4190"
    # process_code="PROC-DAE0E084-FAAD-4415-BA8B-B60523CE5404"
    process_code = "PROC-2C02C3F6-6C98-48B4-94C5-8FEE39D71796"
    # process_code="PROC-A79458C2-6A3F-495C-A955-D77231EBCF29"
    # start_time="1605592791000"
    start_time = int(round(ts * 1000))
    end_time = int(round(tss * 1000))
    arr_list = []
    jps= json.loads(requests.post(
        url="https://oapi.dingtalk.com/topapi/processinstance/listids?access_token=" + access_token + "&process_code=" + process_code + "&start_time=" + str(
            start_time) + "&size=" + str(20)).text)
    # arr_list=jps["result"]["list"]
    for i in range(int(jps["result"]["next_cursor"])):
        arr_list=json.loads(requests.post(
            url="https://oapi.dingtalk.com/topapi/processinstance/listids?access_token=" + access_token + "&process_code=" + process_code + "&start_time=" + str(
                start_time) + "&size=" + str(20)+"&cursor="+str(i)).text)["result"]["list"]+arr_list
    print(len(arr_list))
    # print(arr_list)
    # exit()
    return arr_list



def get_idlist_new(start, end, access_token):
    # 付款单
    dt = str(start) + ' 00:00:00'
    dts = str(end) + ' 23:00:00'
    ts = int(time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S")))
    tss = int(time.mktime(time.strptime(dts, "%Y-%m-%d %H:%M:%S")))
    # access_token=get_token()
    # access_token="0e90cb734b6d397fba82d19577e8c442"
    # process_code="PROC-D449F2F2-CA8B-415D-BFA7-5F49A6F66BBF"
    # process_code="PROC-E3C89E28-5871-4181-AA9C-907EACCC4190"
    # process_code="PROC-DAE0E084-FAAD-4415-BA8B-B60523CE5404"
    process_code = "PROC-3CB7B56C-B650-4307-AE6D-4B9188BEF238"
    # process_code="PROC-A79458C2-6A3F-495C-A955-D77231EBCF29"
    # start_time="1605592791000"
    start_time = int(round(ts * 1000))
    end_time = int(round(tss * 1000))
    return json.loads(requests.post(
        url="https://oapi.dingtalk.com/topapi/processinstance/listids?access_token=" + access_token + "&process_code=" + process_code + "&start_time=" + str(
            start_time) + "&end_time=" + str(end_time)+"&size=20").text)["result"]["list"]


def add_orders(dingding_name, dingding_bumen, dingding_xm, dingding_endtime, dingding_type, xiadan_time, canpin_name,
               canpin_guige, canpin_shu, dd_file, yingyong, zongjia, kdanwei, sfdz, sfr, tel, bz,jn,jnb,cctime,listcode,process_instance_id):

    field_list_ding = [
        "dingding_name",
        "dingding_bumen",
        "dingding_xm",
        "dingding_endtime",
        "dingding_type",
        "xiadan_time",
        "canpin_name_f",
        "canpin_guige_f",
        "canpin_shu_f",
        "yingyong",
        "zongjia",
        "kdanwei",
        "sfdz",
        "sfr",
        "tel",
        "bz",
        "dd_file"


    ]

    # field_list = ["order_id",
    #               "canpin_name",
    #               "canpin_guige",
    #               "canpin_shu",
    #               "orderid",
    #              ]

    # field_list = ["name"]
    # print(dd_file)
    data = get_xiadan("x_orders", str(xiadan_time), 1, 10)
    # print(data)
    if data["code"] == 0:
        return {"msg": "已添加过"}
    value_list1 = []

    value_list1.append(dingding_name)
    value_list1.append(dingding_bumen)
    value_list1.append(dingding_xm)
    if dingding_endtime=="null":
        value_list1.append("")
    else:
        value_list1.append(dingding_endtime)
    value_list1.append(dingding_type)
    value_list1.append(xiadan_time)

    value_list1.append(canpin_name)
    value_list1.append(canpin_guige)
    value_list1.append(canpin_shu)
    # yingyong, zongjia, kdanwei, sfdz, sfr, tel, bz
    value_list1.append(yingyong)
    value_list1.append(zongjia)
    value_list1.append(kdanwei)
    value_list1.append(sfdz)
    value_list1.append(sfr)
    value_list1.append(tel)
    value_list1.append(bz)
    value_list1.append(str(dd_file))

    if jnb and jn:
        dd_ds = get_suser("x_user", None,None, None, 1, 10,str(jn))
        print(dd_ds)
        if dd_ds["code"] == 0:
            field_list_ding.append("caigou_name")
            value_list1.append(str(jn))
            field_list_ding.append("uid")
            value_list1.append(str(dd_ds["data"][0]["id"]))
            field_list_ding.append("cc_time")
            value_list1.append(str(cctime))
            field_list_ding.append("business_id")
            value_list1.append(str(listcode))
            field_list_ding.append("process_instance_id")
            value_list1.append(str(process_instance_id))
        else:
            return 0



    # datas = get_xiadan("x_orders", str(xiadan_time), 1, 10)
    # # print(datas)
    # # print(xiadan_time)
    # orderid = datas["data"][0]["id"]
    #
    #
    # value_list = []
    # for ids in range(1, 1000):
    #     isds = '%03d' % ids
    #     order_id = "XY" + str(time.strftime("%Y%m%d", time.localtime())) + isds
    #     # print(order_id)
    #     datas = get_orderid("x_order", str(order_id), 1, 10)
    #     # print(datas)
    #     if datas["code"] != 0:
    #         break
    # # canpin_name = ops["名称"]
    # # canpin_guige = ops["规格"]
    # # canpin_shu = ops["数量"]
    # value_list.append(order_id)
    #
    # value_list.append(orderid)

    # value_list.append(str(time.strftime("%Y-%m-%d %H.%M.%S", time.localtime())))

    return add_table("x_orders", field_list_ding, value_list1)

def get_data_new(token, listcode):
    # exit()
    # print(requests.get("https://oapi.dingtalk.com/topapi/processinstance/get?access_token="+token+"&process_instance_id="+str(lsits[len(lsits)-1])).text)
    dt = json.loads(requests.get(
        "https://oapi.dingtalk.com/topapi/processinstance/get?access_token=" + token + "&process_instance_id=" + str(
            listcode)).text)
    print(dt)
    op={}
    create_time = dt["process_instance"]["create_time"]
    print(create_time)
    for p in dt["process_instance"]["form_component_values"]:

        try:
            op[p["name"]] = p["value"]
        except:
            pass
    # try:
    print(op["附件"])
    f = json.loads(op["附件"])

    file_list = []
    print(f)
    for i in f:
        file_list.append(get_files_json(token, f, i["fileName"], listcode))

    fujian = file_list
    print(fujian)
    # except:
    #     fujian = ""
    print(op)
    print(fujian)

def get_news():
    token = get_token()
    from datetime import date, timedelta
    tomorrow = (date.today() - timedelta(days=30)).strftime("%Y-%m-%d")
    today = (date.today()).strftime("%Y-%m-%d")
    # tomorrow = "2021-08-01"
    # today = "2021-08-25"
    lsits = get_idlist_new(tomorrow, today, token)
    print(get_data_new(token, lsits[4]))
# get_news()
# exit()

def get_data(token, listcode):
    # exit()
    # print(requests.get("https://oapi.dingtalk.com/topapi/processinstance/get?access_token="+token+"&process_instance_id="+str(lsits[len(lsits)-1])).text)
    dt = json.loads(requests.get(
        "https://oapi.dingtalk.com/topapi/processinstance/get?access_token=" + token + "&process_instance_id=" + str(
            listcode)).text)
    print(dt)

    # print(dt["process_instance"]["title"].split("提交")[0])
    dingding_name = dt["process_instance"]["title"].split("提交")[0]
    #     申请部门（钉钉获取）
    # print(dt["process_instance"]["originator_dept_name"])
    # print(dt["process_instance"]["operation_records"])
    gps = dt["process_instance"]["operation_records"]
    gps2 = dt["process_instance"]["tasks"]
    print(gps)
    # 判断是否被userid用户：010508585133029476 审核
    key = 0
    np=0
    sp=0
    jn = ""
    jnb = ""
    for jpk in gps:
        if jpk["userid"] == "010508585133029476" and jpk["operation_type"] == "REDIRECT_TASK":
            key = 1
            sp = np
        np=np+1
    if key == 0:
        return 0
    print(sp)
    print("------------------------------------")
    if len(gps)>2:
        try:
            if gps[sp+1]["userid"]!="010508585133029476":

                userid_one =str(gps[sp+1]["userid"])
                cc_time =str(gps[sp+1]["finish_time"])
                print(userid_one)
                user_datas=json.loads(requests.get('http://172.16.1.19:8024/dingding/getUserPage?page=1&limit=10&data={"userId":"'+userid_one+'"}').text)
                print(user_datas)
                # try:
                print("-------------111")
                print(user_datas["data"])
                if len(user_datas["data"])>0:


                        jnb = user_datas["data"][0]["jobnumber"]
                        jn = user_datas["data"][0]["name"]
                        print(jnb)
                        print(jn)
                        print("----------------3--------------------")
                else:
                        jn =""
                        jnb=""

        except:
            np2 = 0
            sp2 = 0
            for jpk2 in gps2:
                if jpk2["userid"] == "010508585133029476":

                    sp2 = np2
                np2 = np2 + 1
            try:
                userid_one2 = str(gps2[sp2+1]["userid"])
                cc_time = str(gps2[sp2 + 1]["finish_time"])
                print(userid_one2)
                user_datas2 = json.loads(requests.get(
                    'http://172.16.1.19:8024/dingding/getUserPage?page=1&limit=10&data={"userId":"' + userid_one2 + '"}').text)
                if len(user_datas2["data"]) > 0:
                    jn = user_datas2["data"][0]["name"]
                    jnb = user_datas2["data"][0]["jobnumber"]
                    print(jn)
                    print(jnb)
                    print("----------------3--------------------")
                else:
                    jn = ""
                    jnb = ""

            except:
                pass



    print("-----------------2-------------------")

    print(jnb)
    print(jn)
    if jnb =="" and jn=="":
        return 0
    print("-----------------2-------------------")

    create_time = dt["process_instance"]["create_time"]
    business_id = dt["process_instance"]["business_id"]
    op = {}


    for p in dt["process_instance"]["form_component_values"]:

        try:
            op[p["name"]] = p["value"]
        except:
            pass


    dingding_xm = op["项目名称"]

    dingding_endtime = op["期望交付日期"]
    dingding_type = op["采购类型"]
    dingding_types = json.loads(op["采购明细"])[0]["rowValue"]
    # print(json.loads(op["采购明细"])[0])
    # for k in json.loads(op["采购明细"])[0]["rowValue"]:
    #     print(k)
    # exit()
    # print(dingding_types)
    # exit()
    ops = {}
    for lp in dingding_types:
        ops[lp["label"]] = lp["value"]
    # print(ops)
    # exit()
    try:
        # print(ops["附件"])
        f = ops["附件"]

        file_list=[]
        print(f)
        for i in f:
            file_list.append(get_files_json(token, f, i["fileName"],listcode))





        fujian = file_list
        print(fujian)
    except:
        fujian = ""

    # exit()
    try:
        dingding_bumen = ops["使用部门"]
    except:
        dingding_bumen = ""
    try:

        canpin_name = ops["名称"]
    except:
        canpin_name = ""
    try:
        canpin_guige = ops["规格"]
    except:
        canpin_guige = ""
    try:
        canpin_shu = ops["数量"]
    except:
        canpin_shu = ""
    try:
        yingyong = ops["应用方向（产品/项目）"]
    except:
        yingyong = ""
    try:
        zongjia = ops["预估总价"]
    except:
        zongjia = ""
    try:
        kdanwei = ops["开票单位"][0]
    except:
        kdanwei = ""
    # print(ops)
    try:
        sfdz = ops["收货/使用地址"]
    except:
        sfdz = ""
        # print(ops)
    try:
        sfr = ops["收货人"]
    except:
        sfr = ""
        # print(ops)
    try:
        tel = ops["电话"]
    except:
        tel = ""
        # print(ops)

    try:
        bz = ops["备注"]
    except:
        bz = ""
    print(ops)

    # yingyong,zongjia,kdanwei,sfdz,sfr,tel,bz
    # '应用方向（产品/项目）': '一次性使用取石球囊',
    #
    # '预估总价': '3000',
    # '开票单位': ['宁波新跃医疗科技股份有限公司'],
    # '收货/使用地址': '崇寿老华坤',
    # '收货人': '漆爱国',
    # '电话': '18118157606',
    # '备注': '采购一次性使用取石球囊UV涂胶固化的定位工装，详细信息请见附件图纸和三维模型（STP文件）。\n另外麻烦安排15个工装夹具编码给这个UV涂胶固化的定位工装，用作附件图纸的图号。',

    print("通过")
    # exit()
    # exit()
    # return 1
    return add_orders(dingding_name, dingding_bumen, dingding_xm, dingding_endtime, dingding_type, create_time,
                      canpin_name, canpin_guige, canpin_shu, fujian, yingyong, zongjia, kdanwei, sfdz, sfr, tel, bz,jn,jnb,cc_time,business_id,listcode)

    # print(dt["process_instance"]["form_component_values"][1]["value"])


#
def set_order():
    token = get_token()
    from datetime import date, timedelta

    tomorrow = (date.today() - timedelta(days=120)).strftime("%Y-%m-%d")
    today = (date.today()).strftime("%Y-%m-%d")
    lsits = get_idlist(tomorrow, today, token)
    # print(lsits)
    # exit()
    for vp in lsits:
        print(get_data(token, vp))
    return 1




def get_filess(ff, name):
    token = get_token()
    return get_files_json(token, ff, name)


# ff = [{'spaceId': '886021391', 'fileName': '采购外协申请单-穿刺器TPU粒料-20210622.xls', 'fileSize': 24576, 'fileType': 'xls', 'fileId': '37173506636'}, '76deb917-8db7-4ac8-ac51-f3d9d45df754']
# print(get_filess(ff,"采购外协申请单-穿刺器TPU粒料-20210622.xls"))
# exit()
# print(set_order())
# exit()
#
@app.get('/get_dingding_file')
async def search_phasec(name: str, body: str):
    import ast
    return get_filess(ast.literal_eval(body), name)


@app.get('/get_dingding')
async def search_phasec():
    # try:
    # 前端传输年分 2021  1-12

    data = {
        "code": 0,
        "msg": set_order()

    }
    return data


