"""
Created on 2024/4/17 11:23 
Author: Shuijing
Description: 
"""

from fastapi import APIRouter

from db.models.VersionModel import Version
from tools.ResultResponse import Result

version = APIRouter()


@version.get('/get_latest_Version')
async def get_latest_Version():
    # 返回最新版本
    latest_version = await Version.all().order_by('version_id').first()
    # print(latest_version.version_name)
    return latest_version.version_name
