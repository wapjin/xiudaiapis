# 登录接口
# 已测试
from runs import app
from Model.model_login import login_get
from ..jwts import create_token
@app.get("/login")
async def loginss(users: str, passwd: str):
    df = login_get("x_user", users, passwd)
    if(len(df))>0:
        df =df[0]
        data = {
            "token": str(create_token()),
            "id": df[0],
            "users": df[1],
            "passwd": df[2],
            "name": df[3],
            "gonghao": df[4],
            "zhiwei": df[5],
            "tel": df[6],
            "ctime": str(df[8]).replace("T", " ")

        }
        arr = []
        arr.append(data)
        print(arr)
        return {"code": 0, "msg": "登录成功", "data": arr}

    else:

        return {"code": 1, "msg": "账号或密码错误"}
