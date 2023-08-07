from request_sender import sendRequest

"""
实例文件管理

本项目使用Apache License 2.0开原协议。您在修改、分发本项目中的任意一个文件时，必须阅读、同意并遵守该协议。
This project uses the Apache License 2.0 open source agreement. You must read, agree to, and abide by this agreement when modifying or distributing any of the files in this project.

白墨麒麟Hot / 白墨麒麟 / BaimoQilin / Zhou-Shilin / 周示麟
"""

def get_file_list(url, uuid, remote_uuid, apikey, target, page=0, page_size=40):
    # 获取文件列表
    # 返回类型：json
    # 返回内容解释：详见https://docs.mcsmanager.com/#/zh-cn/apis/instance/view_instance_fils_list

    api_url = url + "/api/files/list"

    """
    uuid: String; // UUID
    apikey: String; // API 密钥
    remote_uuid: String; // 远程服务 UUID
    target: String; //查看的文件目录，如：/xxx
    page: Number  // 第几页，0代表第一页
    page_size: Number // 每页容量，不得超过40
    """

    _paramas = {
        "uuid": uuid,
        "apikey": apikey,
        "remote_uuid": remote_uuid,
        "target": target,
        "page": page,
        "page_size": page_size
    }

    response = sendRequest(api_url, apikey, uuid, remote_uuid, custom_params=_paramas)

    return response

def get_file(url, uuid, remote_uuid, apikey, target):
    # 查看文件
    # 返回类型：json
    # 返回内容解释：文件内容

    api_url = url + "/api/files"

    """
    uuid: String; // UUID
    apikey: String; // API 密钥
    remote_uuid: String; // 远程服务 UUID
    target: String; //查看的文件，如：eula.tx 或 plugins/MyPlugin/config.yml
    page: Number;  // 第几页，0代表第一页
    page_size: Number; // 每页容量，不得超过40
    """

    _body = {
        "target": target
    }

    response = sendRequest(api_url, apikey, uuid, remote_uuid, method="put", body=_body)

    return response["data"]

def edit_file(url, uuid, remote_uuid, apikey, target, text):
    # 编辑文件
    # 返回类型：bool
    # 返回内容解释：True（成功）

    api_url = url + "/api/files"

    """
    uuid: String; // UUID
    apikey: String; // API 密钥
    remote_uuid: String; // 远程服务 UUID
    target: String; // 编辑的文件，如：eula.txt 或 plugins/MyPlugin/config.yml
    text: String; // 文件内容
    """

    _body = {
        "target": target,
        "text": text
    }

    response = sendRequest(api_url, apikey, uuid, remote_uuid, method="put" , body=_body)

    return True

def zip_file(url, uuid, remote_uuid, apikey, target, source):
    # 压缩文件
    # 返回类型：bool
    # 返回内容解释：True（成功）

    api_url = url + "/api/files/compress"

    """
    uuid: String; // UUID
    apikey: String; // API 密钥
    remote_uuid: String; // 远程服务 UUID
    target: List; // 压缩的文件和/或相对目录的列表，如：["usercache.json", "plugins", "world"]
    source: String // 压缩后的文件名，如：BaimoTest.zip
    """

    _body = {
        "type": 1,
        "source": source,
        "targets": target
    }

    response = sendRequest(api_url, apikey, uuid, remote_uuid, method="post", body=_body)

    return True

def unzip_file(url, uuid, remote_uuid, apikey, target, source, code="utf-8"):
    # 解压文件
    # 返回类型：bool
    # 返回内容解释：True（成功）

    api_url = url + "/api/files/compress"

    """
    uuid: String; // UUID
    apikey: String; // API 密钥
    remote_uuid: String; // 远程服务 UUID
    target: String; // 解压后的目录名
    source: String; // 压缩文件名
    code: String // 压缩编码
    """

    _body = {
        "type": 2,
        "source": source,
        "targets": target,
        "code": code
    }

    response = sendRequest(api_url, apikey, uuid, remote_uuid, method="post", body=_body)

    return True

def delete_file(url, uuid, remote_uuid, apikey, target):
    # 解压文件
    # 返回类型：bool
    # 返回内容解释：True（成功）

    api_url = url + "/api/files"

    """
    uuid: String; // UUID
    apikey: String; // API 密钥
    remote_uuid: String; // 远程服务 UUID
    target: List // 要删除的文件和/或相对目录的列表，如：["usercache.json", "plugins", "world"]
    """

    _body = {
        "targets": target
    }

    response = sendRequest(api_url, apikey, uuid, remote_uuid, method="delete", body=_body)

    return True

def move_file(url, uuid, remote_uuid, apikey, source, target):
    # 解压文件
    # 返回类型：bool
    # 返回内容解释：True（成功）

    api_url = url + "/api/files/move"

    """
    uuid: String; // UUID
    apikey: String; // API 密钥
    remote_uuid: String; // 远程服务 UUID
    source: String; // 源文件，如 files.py
    target: String // 目标位置，如 public/files.py
    """

    _body = {
        "targets": [
            [
                source,
                target
            ]
        ]
    }

    response = sendRequest(api_url, apikey, uuid, remote_uuid, method="post", body=_body)

    return True

# 即将上线：文件上传下载功能