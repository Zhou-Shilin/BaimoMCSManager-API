class RequestException(Exception):
    # 请求返回状态码不是200
    pass

class NoThatMethod(Exception):
    # 没有这种请求方式（目前仅支持get, post, push）
    pass
