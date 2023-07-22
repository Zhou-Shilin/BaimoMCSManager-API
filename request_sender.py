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
    elif method == "delete":
        response = requests.delete(api_url, params=_params, headers=_headers, json=body)
    else:
        raise NoThatMethod("内部程序错误：没有这种请求方式（目前仅支持get, post, push, delete）")

    if response.status_code == 200:
        log("(sendRequest) Successful 200")

        return response.json()
    else:
        log("(sendRequest) Failed " + str(response.status_code))

        if response.status_code == 400:
            reason = "参数错误"
        elif response.status_code == 403:
            reason = "无权限"
        elif response.status_code == 500:
            reason = "服务器异常"
        
        raise RequestException("请求返回状态码为" + str(response.status_code) + " " + reason)

        return False
