import requests
from baimomcsm_error import *
from log_writer import log
from time import ctime

def sendRequest(api_url, apikey, uuid=None, remote_uuid=None, method="get", body=None, custom_params=None):
    # 向服务器发送请求
    # 供内部程序使用
    # 返回json

    if custom_params == None:
        _params = {
            "uuid": uuid,
            "remote_uuid": remote_uuid,
            "apikey": apikey
        }
    else:
        _params = custom_params

    _headers = {
        "Content-Type": "application/json; charset=utf-8"
    }

    if method == "get":
        response = requests.get(api_url, params=_params, headers=_headers)
    elif method == "post":
        response = requests.post(api_url, params=_params, headers=_headers, json=body)
    elif method == "put":
        response = requests.put(api_url, params=_params, headers=_headers, json=body)
    else:
        raise NoThatMethod("没有这种请求方式（目前仅支持get, post, push）")

    if response.status_code == 200:
        log("(sendRequest) Successful 200")

        return response.json()
    else:
        log("(sendRequest) Failed " + str(response.status_code))

        raise RequestException("请求返回状态码为" + str(response.status_code))

        return False
