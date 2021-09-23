from runs import app
@app.get("/")
async def read_root():
    return {"msg": "欢迎访问袖带数据调用接口 ！"}