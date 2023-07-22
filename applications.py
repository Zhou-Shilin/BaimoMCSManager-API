from request_sender import sendRequest

"""
应用实例管理

本项目使用Apache License 2.0开原协议。您在修改、分发本项目中的任意一个文件时，必须阅读、同意并遵守该协议。
This project uses the Apache License 2.0 open source agreement. You must read, agree to, and abide by this agreement when modifying or distributing any of the files in this project.

白墨麒麟Hot / 白墨麒麟 / BaimoQilin / Zhou-Shilin / 周示麟
"""

def get_info(url, uuid, remote_uuid, apikey):
    # 获取远程实例详情信息
    # 返回类型：json
    # 返回内容解释：详见https://docs.mcsmanager.com/#/zh-cn/apis/instance/get_instance_info

    api_url = url + "/api/instance"

    response = sendRequest(api_url, apikey, uuid, remote_uuid)

    return response

def get_status(url, uuid, remote_uuid, apikey):
    # 获取远程实例状态
    # 返回类型：int
    # 返回内容解释：-1（状态未知）；0（已停止）；1（正在停止）；2（正在启动）；3（正在运行）

    response = get_info(url, uuid, remote_uuid, apikey)

    data = response["data"]
    status = data["status"]

    return status

def send_command(url, uuid, remote_uuid, apikey, command):
    # 发送命令到应用实例
    # 返回类型：bool
    # 返回内容解释：True（成功）
    # 无法支持命令结果返回，原因请参考：https://github.com/MCSManager/MCSManager/issues/614

    api_url = url + "/api/protected_instance/command"

    send_command_params = {
        "uuid": uuid,
        "remote_uuid": remote_uuid,
        "apikey": apikey,
        "command": command
    }

    response = sendRequest(api_url, apikey, uuid, remote_uuid, method="put",custom_params=send_command_params)

    return True

def get_outputlog(url, uuid, remote_uuid, apikey):
    # 开启实例
    # 返回类型：str
    # 返回内容解释：日志输出

    api_url = url + "/api/protected_instance/outputlog"

    response = sendRequest(api_url, apikey, uuid, remote_uuid)

    data = response["data"]

    return data

def start_app(url, uuid, remote_uuid, apikey):
    # 开启实例
    # 返回类型：bool
    # 返回内容解释：True（成功）

    api_url = url + "/api/protected_instance/open"

    response = sendRequest(api_url, apikey, uuid, remote_uuid)

    return True

def stop_app(url, uuid, remote_uuid, apikey):
    # 关闭实例
    # 返回类型：bool
    # 返回内容解释：True（成功）

    api_url = url + "/api/protected_instance/stop"

    response = sendRequest(api_url, apikey, uuid, remote_uuid)

    return True

def restart_app(url, uuid, remote_uuid, apikey):
    # 重启实例
    # 返回类型：bool
    # 返回内容解释：True（成功）

    api_url = url + "/api/protected_instance/restart"

    response = sendRequest(api_url, apikey, uuid, remote_uuid)

    return True

def kill_app(url, uuid, remote_uuid, apikey):
    # 强制关闭实例
    # 返回类型：bool
    # 返回内容解释：True（成功）

    api_url = url + "/api/protected_instance/kill"

    response = sendRequest(api_url, apikey, uuid, remote_uuid)

    return True