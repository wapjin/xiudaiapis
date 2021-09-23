from runs import app
from fastapi import  File, UploadFile
from fastapi.responses import StreamingResponse
from starlette.responses import FileResponse
from Model.adddata import add_table
from Model.getdata import danwei_s_list1
from Model.updata import up_table
import os,xlrd,time
# 附件上传接口
# 已测试
# 上传文件
@app.post("/danwei_up_file")
async def create_file(file: UploadFile = File(...)):
    # try:
        print(os.getcwd())
        pas = os.getcwd().split("\Controller\Controller_all_xinxi")
        res = await file.read()
        print(pas)
        print(os.path.join(pas[0], "files",file.filename ))
        f = open(os.path.join(pas[0], "files",file.filename ), "wb+")
        f.write(res)
        f.close()
        file = xlrd.open_workbook(os.path.join(pas[0], "files",file.filename ))  # 打开Excel文件
        sheet_1 = file.sheet_by_index(0)  # 根据sheet页的排序选取sheet
        # row_content = sheet_1.row_values(3)  # 获取指定行的数据，返回列表，排序自0开始
        row_number = sheet_1.nrows  # 获取有数据的最大行数
        arrt = []
        for ij in range(row_number):
            arrt.append(sheet_1.row_values(ij))
        arr_chong=[]
        for v in range(len(arrt)):
            if v>0:
                print(arrt[v][0])
                dt = danwei_s_list1("gonhuo_xinxi",str(arrt[v][0]),None,None,None,1, 100)
                print(dt)
                if dt["code"]==0:
                   
                    value_list = []
                    value_list.append(arrt[v][0])
                    try:
                        value_list.append(arrt[v][1])
                    except:
                        value_list.append("")
                    try:
                        value_list.append(int(arrt[v][2]))
                    except:
                        value_list.append(arrt[v][2])
                    try:
                        value_list.append(int(arrt[v][3]))
                    except:
                        value_list.append(arrt[v][3])
                        
                    try:    
                        value_list.append(arrt[v][4])
                    except:
                        value_list.append("")
                    try:
                        value_list.append(int(arrt[v][5]))
                    except:
                        value_list.append(arrt[v][5])
                    try:
                        value_list.append(arrt[v][6])
                    except:
                        value_list.append("")
                    try:
                        value_list.append(arrt[v][7])
                    except:
                        value_list.append("")
                    try:
                        value_list.append(arrt[v][8])
                    except:
                        value_list.append("")
                    try:
                        value_list.append(arrt[v][9])
                    except:
                        value_list.append("")
                    try:
                        value_list.append(arrt[v][10])
                    except:
                        value_list.append("")
                    try:
                        value_list.append(arrt[v][11])
                    except:
                        value_list.append("")
                    field = "gonghuo_danwe='" + str(value_list[0]) + "',gonghuo_name='" + str(value_list[1]) +\
                            "',gonghuo_itel='" + str(value_list[2]) + "',gonghuo_gtel='" + str(value_list[3]) +\
                            "',gonghuo_dizhi='" + str(value_list[4]) + "',gonghuo_cz='" + str(value_list[5]) + "'"
        
                    up_table("gonhuo_xinxi",field,dt["data"][0]["id"])
               
               
                else:
             
                    field_list = ["gonghuo_danwe", "gonghuo_name", "gonghuo_itel", "gonghuo_gtel", "gonghuo_dizhi",
                                  "gonghuo_cz","remark_1","remark_2","remark_3","remark_4","remark_5","remark_6",
                                  "ctime"]
                    value_list = []
                    value_list.append(arrt[v][0])
                    try:
                        value_list.append(arrt[v][1])
                    except:
                        value_list.append("")
                    try:
                        value_list.append(int(arrt[v][2]))
                    except:
                        value_list.append(arrt[v][2])
                    try:
                        value_list.append(int(arrt[v][3]))
                    except:
                        value_list.append(arrt[v][3])
                        
                    try:    
                        value_list.append(arrt[v][4])
                    except:
                        value_list.append("")
                    try:
                        value_list.append(int(arrt[v][5]))
                    except:
                        value_list.append(arrt[v][5])
                    try:
                        value_list.append(arrt[v][6])
                    except:
                        value_list.append("")
                    try:
                        value_list.append(arrt[v][7])
                    except:
                        value_list.append("")
                    try:
                        value_list.append(arrt[v][8])
                    except:
                        value_list.append("")
                    try:
                        value_list.append(arrt[v][9])
                    except:
                        value_list.append("")
                    try:
                        value_list.append(arrt[v][10])
                    except:
                        value_list.append("")
                    try:
                        value_list.append(arrt[v][11])
                    except:
                        value_list.append("")
               
                    value_list.append(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
                    # field = "name='" + str(str(time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))) + "'"
                    add_table("gonhuo_xinxi", field_list, value_list)
        strs=""
        for pd in arr_chong:
            strs=pd+","+strs
        if len(arr_chong)==0:
            return {"code":0,"msg": "导入成功"}
        else:
            
            return {"code":0,"msg": strs+"，重复了！"}
    # except:
    #     return {"msg": "上传失败"}
# 访问文件
@app.get("/get_file_danwei")
async def create_files():

    # try:
        name="gongyin.xls"
        pas = os.getcwd().split("\Controller\Controller_all_xinxi")
        # print(os.path.join(pas[0], "files", name))
        # file_like = open(os.path.join(pas[0], "files",name ), mode="rb")
        # return FileResponse(os.path.join(pas[0], "files",name ),filename=name)
        #  pas = os.getcwd().split("\Controller\Controller_order")
        drs = os.path.join(pas[0], "files", name)
        # file_like = open(, mode="rb")
        return FileResponse(drs,filename=name)
        # return StreamingResponse(file_like)
    # except:
    #     # file_like = open('file/1.jpg', mode="rb")
    #     return {"msg": "没有此文件"}