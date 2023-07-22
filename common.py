from request_sender import sendRequest

"""
面板通用设置

本项目使用Apache License 2.0开原协议。您在修改、分发本项目中的任意一个文件时，必须阅读、同意并遵守该协议。
This project uses the Apache License 2.0 open source agreement. You must read, agree to, and abide by this agreement when modifying or distributing any of the files in this project.

白墨麒麟Hot / 白墨麒麟 / BaimoQilin / Zhou-Shilin / 周示麟
"""

def get_overview(url, apikey):
    # 数据监控
    # 返回类型：json
    # 返回内容解释：详见https://docs.mcsmanager.com/#/zh-cn/apis/panel/overview

    api_url = url + "/api/overview"

    response = sendRequest(api_url, apikey)

    return response

def get_remote_services_system_overview(url, apikey):
    # 查看面板数据简报
    # 返回类型：json
    # 返回内容解释：详见https://docs.mcsmanager.com/#/zh-cn/apis/remote/get_remote_services_info

    api_url = url + "/api/service/remote_services_system"

    response = sendRequest(api_url, apikey)

    return response

def get_settings(url, apikey):
    # 获取面板设置
    # 返回类型：json
    # 返回内容解释：详见https://docs.mcsmanager.com/#/zh-cn/apis/panel/get_settings

    api_url = url + "/api/overview/setting"

    response = sendRequest(api_url, apikey)

    return response

def edit_settings(url, apikey, httpPort="25566", httpIP=None, dataPort=23334, forwardType=1, crossDomain=False, gzip=False, maxCompress=1, maxDonwload=10, zipType=1, loginCheckIp=True, loginInfo="", canFileManager=True, language="en_us", quickInstallAddr="https://mcsmanager.oss-cn-guangzhou.aliyuncs.com/quick_install.json", redisUrl=""):
    # 修改面板设置
    # 返回类型：bool
    # 返回内容解释：True（成功）

    api_url = url + "/api/overview/setting"

    _body = {
        'httpPort': httpPort, 
        'httpIp': httpIP, 
        'dataPort': dataPort, 
        'forwardType': forwardType, 
        'crossDomain': crossDomain, 
        'gzip': gzip, 
        'maxCompress': maxCompress, 
        'maxDonwload': maxDonwload, 
        'zipType': zipType, 
        'loginCheckIp': loginCheckIp, 
        'loginInfo': loginInfo, 
        'canFileManager': canFileManager, 
        'language': language, 
        'quickInstallAddr': quickInstallAddr, 
        'redisUrl': redisUrl
    }

    response = sendRequest(api_url, None, None, apikey, method="put",body=_body)

    return True
