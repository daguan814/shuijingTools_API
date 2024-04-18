"""
Created on 2024/4/11 15:31 
Author: Shuijing
Description: 
"""
from tortoise.models import Model
from tortoise import fields


class Version(Model):
    version_id = fields.IntField(pk=True, description="版本id,主要是知道是第几次更新版本")
    version_name = fields.CharField(max_length=50, description="版本名")
