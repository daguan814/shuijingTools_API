"""
Created on 2024/4/16 09:37 
Author: Shuijing
Description: 
"""

from tools.ResultResponse import Result
from fastapi import APIRouter, Request


net = APIRouter()


@net.get('/netCheck', response_model=Result)
def netCheck(request: Request):
    # 需要检查的 IP 前缀列表
    ip_prefixes = [
        '10.11',
        # '192.168',
        # '127.0.0.1'
    ]
    client_host = request.client.host
    for prefix in ip_prefixes:
        if client_host.startswith(prefix):
            return Result(code=200, msg='正常ip', data=[{'ip': client_host}])

    # 如果未找到匹配的前缀，则返回默认消息和代码
    return Result(code=100, msg='不正常ip', data=[{'ip': client_host}])
