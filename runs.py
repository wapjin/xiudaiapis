from fastapi import FastAPI, Header, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# 跨域访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from Controller import *
# 启动入口
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8400)