from runs import app
from fastapi import  File, UploadFile
from fastapi.responses import StreamingResponse
import os
# 附件上传接口
# 已测试
# 上传文件
@app.post("/up_file")
async def create_file(file: UploadFile = File(...)):
    try:
        pas = os.getcwd().split("\Controller\Controller_order")
        res = await file.read()
        print(os.path.join(pas[0], "files",file.filename ))
        f = open(os.path.join(pas[0], "files",file.filename ), "wb+")
        f.write(res)
        return {"msg": "上传成功","url":"/file?name="+str(file.filename)}
    except:
        return {"msg": "上传失败"}


# 访问文件
@app.get("/file")
async def create_files(name: str = None):

    try:
        pas = os.getcwd().split("\Controller\Controller_order")
        print(os.path.join(pas[0], "files", name))
        file_like = open(os.path.join(pas[0], "files",name ), mode="rb")
        return StreamingResponse(file_like)
    except:
        # file_like = open('file/1.jpg', mode="rb")
        return {"msg": "没有此文件"}


# print(os.path.dirname(os.path.realpath(__file__)))
# print()