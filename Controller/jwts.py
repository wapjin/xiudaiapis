import time


# 将上面生成的 jwt 进行解析认证json
def jwts(jwt_token):
    try:
        import base64
        s = base64.b64decode(jwt_token)
        # print(s)
        if int(s) > int(time.time()):

            return 1
        else:

            return '身份验证过期'
    except:
        return '身份验证过期'


def create_token():

    import base64
    ts =str(int(time.time()) + 3600)
    # print(ts)
    s = base64.b64encode(ts.encode()).decode()
    return s


print(create_token())
#
# jwt_token = b'MTYyMDcxMjk0NA=='
# print(jwts(jwt_token))