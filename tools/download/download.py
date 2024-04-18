"""
Created on 2024/4/16 11:13 
Author: Shuijing
Description: 
"""
import os

from starlette.responses import FileResponse

from tools.ResultResponse import Result
from fastapi import APIRouter, Request
from pydantic import BaseModel

download = APIRouter()


# 提供要下载的文件

