"""
Created on 2024/4/9 10:14 
Author: Shuijing
Description: 
"""
from tortoise.models import Model
from tortoise import fields
class File(Model):
    fileid = fields.IntField(pk=True, description='上传文件的id,四位数字')
    username = fields.CharField(max_length=40, description='上传用户的名字')
    filename = fields.CharField(max_length=50, description='文件名,id加原始文件名')
    upload_time = fields.DatetimeField(auto_now_add=True, description='上传时间')
    download_time = fields.DatetimeField(auto_now=True, description='最后一次下载的时间')
    download_count = fields.IntField(default=0, description='下载次数')
