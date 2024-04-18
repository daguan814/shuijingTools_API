"""
Created on 2024/4/9 10:14 
Author: Shuijing
Description: 
"""
from tortoise.models import Model
from tortoise import fields


class File(Model):
    file_id = fields.IntField(pk=True, description='文件id')
    file_name = fields.CharField(max_length=50,  description='文件名')
    upload_time = fields.DatetimeField(auto_now_add=True, description='上传时间')
    download_time = fields.DatetimeField(auto_now=True, description='最后一次下载的时间')
    download_count = fields.IntField(default=0, description='下载次数')
    file_type = fields.CharField(max_length=20, description='文件类型,安装包或者压缩包')
    file_size = fields.CharField(max_length=20, description='文件大小,以MB为单位')
