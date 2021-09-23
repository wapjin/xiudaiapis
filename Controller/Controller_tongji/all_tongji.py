from runs import app
from fastapi import  Header
from pydantic import BaseModel
from ..jwts import jwts
from Model.getdata import get_tongji,get_tongjis,get_tongjigg,getid
import json
# 统计金额
# 未测试

def datas(jaon):
    arr_name_list=[]
    for i in jaon:
        if i["xm"] not in arr_name_list:
            arr_name_list.append(i["xm"])

    p={}
    for t in arr_name_list:
        arr2 = []
        for i in jaon:
            if i["xm"]==t:
                arr2.append(i)
        p[t]=arr2

    print(p)
    # exit()
    for ap in p:
        ipss={}
        for ipsss in range(12):
            ipss["jia" + str(ipsss)] = 0
        for ips in p[ap]:
            for i in range(12):

                ipss["jia" + str(i)] = ips["jia" + str(i)]+ipss["jia" + str(i)]
            ipss["xmhe"]=ips["xmhe"]
        ipss["xm"]=ap
        p[ap]=ipss
    att_data_p=[]
    for k in p:
        att_data_p.append(p[k])

    return att_data_p

def get_tongjiss(yer,yue):
    yer_tyue=str(yer)+"-"+str(yue)
    print("------")
    print(yer_tyue)
    table="x_orders"
    s = get_tongjigg(table)
    print("------")
    print(s)
    print("------")
    arr_xm=[]
    arr_xms=[]
    if s["code"]==0:
        for i in s["data"]:
            arr_xm.append(i["id"])
            arr_xms.append(i["dingding_xm"])
        news_ids = []
        news_idss = []
        for id in arr_xm:
            if id not in news_ids:
                news_ids.append(id)
        for ids in arr_xms:
            if ids not in news_idss:
                news_idss.append(ids)
        print(news_ids)
        arrs=[]
        table="x_order"
        for k in news_ids:
            ks={}
            s1 = get_tongjis(table, yer_tyue, "yufu_time", k,"orderid")
            s2 = get_tongjis(table, yer_tyue, "zhongqi_time", k,"orderid")
            s3 = get_tongjis(table, yer_tyue, "yukuan_time", k,"orderid")
            unm=0
            ks[k] = unm
            if s1["code"] == 0:
                for so in s1["data"]:
                    if so["yufu_kuan"]:
                        try:
                            s1g = float(so["yufu_kuan"])
                        except:
                            s1g=0
                    else:
                        s1g=0
                    ks[k] = s1g+float(ks[k])
                    print(so)
                    print(1)

            if s2["code"] == 0:
                for so2 in s2["data"]:
                    # ks[k] = float(so2["zhongqi_kuan"]) + ks[k]
                    if so2["zhongqi_kuan"]:
                        try:
                            s2g = float(so2["zhongqi_kuan"])
                        except:
                            s2g=0
                    else:
                        s2g=0
                    ks[k] = s2g+float(ks[k])
                    print(so2)
                    print(2)

            if s3["code"] == 0:
                for so3 in s3["data"]:
                    # ks[k] = float(so3["yukuan"]) + ks[k]
                    if so3["yukuan"]:
                        try:
                            s3g = float(so3["yukuan"])
                        except:
                            s3g=0
                    else:
                        s3g=0
                    ks[k] = s3g+float(ks[k])
                    # zhongqi_kuan
                    print(so3)
                    print(3)
            # print(num)

            arrs.append(ks)
        return arrs,news_ids
    else:
        return [],[]
    # print(s)
    # print(s)
    # print(s)



def alltongji(yess):

    # if yue:
    #
    #     if caigou_name:
    #
    #         sp = get_tongjiss(yess, yue,caigou_name,None,None)
    #         at = []
    #         print(sp)
    #         # print(sp[0][0]["202-Ercp项目"])
    #         # # print(sp[0]["202-Ercp项目"])
    #         # exit()
    #         for p in range(len(sp[1])):
    #             o = {}
    #
    #             o["xm"] = sp[1][p]
    #
    #             o["jia"] = sp[0][p][sp[1][p]]
    #
    #             at.append(o)
    #
    #         return at
    #
    #         pass
    #     elif gongyi_name:
    #         sp = get_tongjiss(yess, yue, None, gongyi_name, None)
    #         at = []
    #         print(sp)
    #         # print(sp[0][0]["202-Ercp项目"])
    #         # # print(sp[0]["202-Ercp项目"])
    #         # exit()
    #         for p in range(len(sp[1])):
    #             o = {}
    #
    #             o["xm"] = sp[1][p]
    #
    #             o["jia"] = sp[0][p][sp[1][p]]
    #
    #             at.append(o)
    #
    #         return at
    #
    #         pass
    #     elif xm_name:
    #         sp = get_tongjiss(yess, yue, None, None, xm_name)
    #         at = []
    #         print(sp)
    #         # print(sp[0][0]["202-Ercp项目"])
    #         # # print(sp[0]["202-Ercp项目"])
    #         # exit()
    #         for p in range(len(sp[1])):
    #             o = {}
    #
    #             o["xm"] = sp[1][p]
    #
    #             o["jia"] = sp[0][p][sp[1][p]]
    #
    #             at.append(o)
    #
    #         return at
    #         pass
    #     else:
    #
    #         sp= get_tongjiss(yess, yue,None,None,None)
    #         at=[]
    #         print(sp)
    #         # print(sp[0][0]["202-Ercp项目"])
    #         # # print(sp[0]["202-Ercp项目"])
    #         # exit()
    #         for p in range(len(sp[1])):
    #             o = {}
    #
    #             o["xm"] = sp[1][p]
    #
    #             o["jia"] = sp[0][p][sp[1][p]]
    #
    #             at.append(o)
    #
    #         return at

    arg =[]
    arrs =get_tongjiss(yess,"01")[1]
    # print(arrs)
    for ids in range(1,13):
            isds = '%02d' % ids
            print(isds)
            arg.append(get_tongjiss(yess,isds)[0])
    # print(arg)
    # print(arrs)
    arr1y=[]
    for yu in arg:
        ss=0
        for p in yu:
            for ps in arrs:
                try:
                    ss = float(p.get(ps))+ss
                except:
                    pass
        arr1y.append(ss)
    # 每月合计价格

    arr100 = []
    for xm in arrs:


        dx = {}
        for er in range(len(arg)):

            for y in arg[er]:
                print(y)

                print(y.get(str(xm)))

                if y.get(xm)!=None:

                    dx["jia"+str(er)] = y.get(xm)
                    mx_data = getid("x_orders",xm)
                    dx["xm"] = mx_data["data"][0]["dingding_xm"]

                    # arr2.append(dx)
        print(dx)
        
        

        arr100.append(dx)
    for ty in arr100:
        s=0
        for pf in range(12):
            try:
                s = ty.get("jia"+str(pf))+s
            except:
                s=0
        ty["xmhe"]=s
    h={}
    ssd = 0

    print(arr1y)
    for pf in range(12):
        h["jia"+str(pf)]=arr1y[pf]
        ssd=arr1y[pf]+ssd
        h["xmhe"] = ssd
        h["xm"] = "汇总"

    arr100.append(h)
    print(arr100)
    
    
    return arr100

            # try:
            #     dx["jia"]=y[xm]
            #     dx["xm"]=xm
            # except:
            #     dx["jia"] = 0
            #     dx["xm"] = xm

    # print(arr)

def get_tongjiss1(yer,yue):
    yer_tyue=str(yer)+"-"+str(yue)
    print("------")
    print(yer_tyue)
    table="x_order"
    s = get_tongji(table,str(yer),"yufu_time")
    arr_xm=[]
    if s["code"]==0:
        for i in s["data"]:
            arr_xm.append(i["caigou_name"])
        print(arr_xm)
        news_ids = []
        for id in arr_xm:
            if id not in news_ids:
                if id:
                    news_ids.append(id)
        print(news_ids)
        arrs=[]
        for k in news_ids:
            ks={}
            s1 = get_tongjis(table, yer_tyue, "yufu_time", k,"caigou_name")
            s2 = get_tongjis(table, yer_tyue, "zhongqi_time", k,"caigou_name")
            s3 = get_tongjis(table, yer_tyue, "yukuan_time", k,"caigou_name")
            unm=0
            ks[k] = unm
            if s1["code"] == 0:
                for so in s1["data"]:
                    if so["yufu_kuan"]:
                        try:
                            s1g = float(so["yufu_kuan"])
                        except:
                            s1g=0
                    else:
                        s1g=0
                    ks[k] = s1g+float(ks[k])
                    print(so)
                    print(1)

            if s2["code"] == 0:
                for so2 in s2["data"]:
                    # ks[k] = float(so2["zhongqi_kuan"]) + ks[k]
                    if so2["zhongqi_kuan"]:
                        try:
                            s2g = float(so2["zhongqi_kuan"])
                        except:
                            s2g=0
                    else:
                        s2g=0
                    ks[k] = s2g+float(ks[k])
                    print(so2)
                    print(2)

            if s3["code"] == 0:
                for so3 in s3["data"]:
                    # ks[k] = float(so3["yukuan"]) + ks[k]
                    if so3["yukuan"]:
                        try:
                            s3g = float(so3["yukuan"])
                        except:
                            s3g=0
                    else:
                        s3g=0
                    ks[k] = s3g+float(ks[k])
                    # zhongqi_kuan
                    print(so3)
                    print(3)
            # print(num)

            arrs.append(ks)
        return arrs,news_ids
    else:
        return [],[]
    # print(s)
    # print(s)
    # print(s)



def alltongji1(yess):



    arg =[]
    arrs =get_tongjiss1(yess,"01")[1]
    for ids in range(1,13):
            isds = '%02d' % ids
            print(isds)
            arg.append(get_tongjiss1(yess,isds)[0])
    # print(arg)
    # print(arrs)
    arr1y=[]
    for yu in arg:
        ss=0
        for p in yu:
            for ps in arrs:
                try:
                    ss = float(p.get(ps))+ss
                except:
                    pass
        arr1y.append(ss)
    # 每月合计价格

    arr100 = []
    for xm in arrs:


        dx = {}
        for er in range(len(arg)):

            for y in arg[er]:
                print(y)

                print(y.get(str(xm)))

                if y.get(xm)!=None:

                    dx["jia"+str(er)] = y.get(xm)
                    dx["xm"] = xm

                    # arr2.append(dx)
        print(dx)

        arr100.append(dx)
    for ty in arr100:
        s=0
        for pf in range(12):
            try:
                s = ty.get("jia"+str(pf))+s
            except:
                s=0
        ty["xmhe"]=s
    h={}
    ssd = 0

    print(arr1y)
    for pf in range(12):
        h["jia"+str(pf)]=arr1y[pf]
        ssd=arr1y[pf]+ssd
        h["xmhe"] = ssd
        h["xm"] = "汇总"

    arr100.append(h)
    print(arr100)
    return arr100

            # try:
            #     dx["jia"]=y[xm]
            #     dx["xm"]=xm
            # except:
            #     dx["jia"] = 0
            #     dx["xm"] = xm

    # print(arr)


def get_tongjiss2(yer, yue):
    yer_tyue = str(yer) + "-" + str(yue)
    print("------")
    print(yer_tyue)
    table = "x_order"
    s = get_tongji(table, str(yer), "yufu_time")
    arr_xm = []
    if s["code"] == 0:
        print(s["data"])
        for i in s["data"]:
            arr_xm.append(i["gonghuo_danwe"])
        news_ids = []
        for id in arr_xm:
            if id not in news_ids:
                if id:
                    news_ids.append(id)
        print(news_ids)
        arrs = []
        for k in news_ids:
            ks = {}
            s1 = get_tongjis(table, yer_tyue, "yufu_time", k, "gonghuo_danwe")
            s2 = get_tongjis(table, yer_tyue, "zhongqi_time", k, "gonghuo_danwe")
            s3 = get_tongjis(table, yer_tyue, "yukuan_time", k, "gonghuo_danwe")
            unm = 0
            ks[k] = unm
            if s1["code"] == 0:
                for so in s1["data"]:
                    if so["yufu_kuan"]:
                        try:
                            s1g = float(so["yufu_kuan"])
                        except:
                            s1g=0
                    else:
                        s1g=0
                    ks[k] = s1g+float(ks[k])
                    print(so)
                    print(1)

            if s2["code"] == 0:
                for so2 in s2["data"]:
                    # ks[k] = float(so2["zhongqi_kuan"]) + ks[k]
                    if so2["zhongqi_kuan"]:
                        try:
                            s2g = float(so2["zhongqi_kuan"])
                        except:
                            s2g = 0
                    else:
                        s2g=0
                    ks[k] = s2g+float(ks[k])
                    print(so2)
                    print(2)

            if s3["code"] == 0:
                for so3 in s3["data"]:
                    # ks[k] = float(so3["yukuan"]) + ks[k]
                    if so3["yukuan"]:
                        try:
                            s3g = float(so3["yukuan"])
                        except:
                            s3g = 0
                    else:
                        s3g=0
                    ks[k] = s3g+float(ks[k])
                    # zhongqi_kuan
                    print(so3)
                    print(3)
            # print(num)

            arrs.append(ks)
        return arrs, news_ids
    else:
        return [], []
    # print(s)
    # print(s)
    # print(s)


def alltongji2(yess):
    arg = []
    arrs = get_tongjiss2(yess, "01")[1]
    for ids in range(1, 13):
        isds = '%02d' % ids
        print(isds)
        arg.append(get_tongjiss2(yess, isds)[0])
    # print(arg)
    # print(arrs)
    arr1y = []
    for yu in arg:
        ss = 0
        for p in yu:
            for ps in arrs:
                try:
                    ss = float(p.get(ps)) + ss
                except:
                    pass
        arr1y.append(ss)
    # 每月合计价格

    arr100 = []
    for xm in arrs:

        dx = {}
        for er in range(len(arg)):

            for y in arg[er]:
                print(y)

                print(y.get(str(xm)))

                if y.get(xm) != None:
                    dx["jia" + str(er)] = y.get(xm)

                    dx["xm"] = xm

                    # arr2.append(dx)
        print(dx)

        arr100.append(dx)
    for ty in arr100:
        s = 0
        for pf in range(12):
            s = ty.get("jia" + str(pf)) + s
        ty["xmhe"] = s
    h = {}
    ssd = 0

    print(arr1y)
    for pf in range(12):
        h["jia" + str(pf)] = arr1y[pf]
        ssd = arr1y[pf] + ssd
        h["xmhe"] = ssd
        h["xm"] = "汇总"

    arr100.append(h)
    print(arr100)
    return arr100


# print(alltongji(2021))
# print(alltongji1(2021))
# print(alltongji2(2021))
# exit()
import time
@app.get('/all_tongji')
async def search_phasec(*, Authorization: str = Header(None),yess:str,types:str):
    # try:   ①采购员②供应商③项目④整体
    # 前端传输年分 2021  1-12
    msg = jwts(Authorization)
    print(msg)
    if msg == 1:
        if yess=="":
            yess=str(time.strftime("%Y", time.localtime()))
        if types=="":
            types="1"
        if types=="1":
            data={

                "code":0,
                "data":datas(alltongji(yess))

            }
        elif types=="2":
            data={

                "code":0,
                "data":alltongji1(yess)

            }
        elif types == "3":
            data = {

                "code": 0,
                "data": alltongji2(yess)

            }
        else:
           data = {

                "code": 0,
                "data": datas(alltongji(yess))

            } 
        return data



    else:
        return {"code": 1001, "msg": msg}
# alltongji(2021)