from request_sender import sendRequest

"""
多用户设置

本项目使用Apache License 2.0开原协议。您在修改、分发本项目中的任意一个文件时，必须阅读、同意并遵守该协议。
This project uses the Apache License 2.0 open source agreement. You must read, agree to, and abide by this agreement when modifying or distributing any of the files in this project.

白墨麒麟Hot / 白墨麒麟 / BaimoQilin / Zhou-Shilin / 周示麟
"""

def create_user(url, apikey, username, password, permission):
    # 创建用户
    # 返回类型：bool
    # 返回内容解释：True（成功）

    # 参数说明：
    # username: 用户名
    # password: 密码
    # permission: -1（封禁）；1（普通权限）；10（最高权限）

    api_url = url + "/api/overview/setting"

    _body = {
        'username': username, 
        'password': password, 
        'permission': permission, 
    }

    response = sendRequest(api_url, apikey, method="post", body=_body)

    return True

def delete_user(url, apikey, uuid):
    # 删除用户
    # 返回类型：bool
    # 返回内容解释：True（成功）

    # 参数说明：
    # uuid: 需要删除的用户的uuid，可以指定多个 例：["uuid", "uuid2", "uuid3"]

    api_url = url + "/api/overview/setting"

    _body = {
        uuid
    }

    response = sendRequest(api_url, apikey, method="delete", body=_body)

    return True

def get_overview(url, apikey):
    # 用户数据总览
    # 返回类型：json
    # 返回内容解释：详见https://docs.mcsmanager.com/#/zh-cn/apis/panel/user_overview

    api_url = url + "/api/auth/overview"

    response = sendRequest(api_url, apikey)

    return response

def get_info(url, apikey, uuid, advanced=True):
    # 查看用户数据
    # 返回类型：json
    # 返回内容解释：详见https://docs.mcsmanager.com/#/zh-cn/apis/panel/info

    # 参数说明
    # uuid：用户uuid

    _body = {
        "apikey": apikey,
        "advanced": advanced,
        "uuid": uuid
    }

    api_url = url + "/api/auth/"

    response = sendRequest(api_url, apikey, body=_body)

    return response

def update_user_settings(url, apikey, uuid, permission, instance):
    # 更改用户信息
    # 返回类型：bool
    # 返回内容解释：True（成功）

    # 参数说明：
    # uuid: 用户uuid
    # perimission: -1（封禁）；1（普通权限）；10（最高权限）
    # instance: 用户可以控制的实例，列表。例：
    """
    // 目标用户能管理的实例，分别是守护进程UUID，实例UUID
    [
      {
        "serviceUuid": "0e865f1f14c14906894698cc71f4e574",
        "instanceUuid": "11e2f159b43f447eacb213b2cdc6df2a"
      },
      {
        "serviceUuid": "07027a72d147487aa0a2ca0616231f22",
        "instanceUuid": "11e2f159b43f447eacb213b2cdc6df2a"
      },
      {
        "serviceUuid": "0e865f1f14c14906894698cc71f4e574",
        "instanceUuid": "11e2f159b43f447eacb213b2cdc6df2a"
      }
    ]"""


    api_url = url + "/api/auth"


    _body = {
        "uuid": uuid,
        "config": {
            "permission": permission,
            "instances": instance
        }
    }

    response = sendRequest(api_url, apikey, method="put", body=_body)

    return response

