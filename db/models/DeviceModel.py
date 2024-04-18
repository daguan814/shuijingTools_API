"""
Created on 2024/4/11 15:19 
Author: Shuijing
Description: 
"""
from tortoise.models import Model
from tortoise import fields


class Device(Model):
    device_id = fields.IntField(pk=True, description='设备id')
    device_name = fields.CharField(max_length=50, description='设备名')
    another_info = fields.CharField(max_length=200, description='其余说明', null=True, blank=True)
    address_mac = fields.CharField(max_length=40, description='mac地址')
    address_ip = fields.CharField(max_length=40, description='ip地址')
    first_send_time = fields.DatetimeField(auto_now_add=True, description='第一次报告时间')
