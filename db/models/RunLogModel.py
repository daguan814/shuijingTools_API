"""
Created on 2024/4/11 15:27 
Author: Shuijing
Description: 
"""
from tortoise.models import Model
from tortoise import fields


class RunLog(Model):
    log_id = fields.IntField(pk=True, description='日志id')
    device_name = fields.CharField(max_length=50, description='设备名')
    log_time = fields.DatetimeField(auto_now_add=True, description='日志产生时间')
    log_type = fields.CharField(max_length=50, description='日志重要程度')
    log_message = fields.CharField(max_length=200, description='日志信息')
