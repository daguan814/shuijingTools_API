"""
Created on 2024/4/16 14:20 
Author: Shuijing
Description: 
"""
import os.path

from fastapi import APIRouter
from starlette.responses import FileResponse

from Routes.file.fileService import get_file_size
from db.models.FileModel import File
from tools.ResultResponse import Result
from fastapi import UploadFile

file_api = APIRouter()


@file_api.post("/upload", response_model=Result)  # 单文件上传
async def upload_file(file: UploadFile, file_type: str):
    try:
        # 文件保存路径
        path = os.path.join('uploads', file.filename)

        # 文件保存
        with open(path, 'wb') as f:
            for line in file.file:
                f.write(line)

        # 获取文件大小并转换为MB格式（保留1位小数）
        file_size_mb = "{:.1f}".format(get_file_size(path))
        file_size_with_unit = f"{file_size_mb} MB"

        # 文件信息写入数据库
        file_info = File(file_name=file.filename, file_type=file_type, file_size=file_size_with_unit)
        await file_info.save()

        data = [{"filename": file.filename, "file_size": file_size_with_unit}]
        return Result(code=200, msg="上传成功", data=data)
    except Exception as e:
        print("上传文件失败:", e)
        return Result(code=500, msg="上传失败", data=None)


@file_api.get("/download/{file_name}")
async def download_tools(file_name: str):
    # 拼接文件路径
    file_path = os.path.join(os.getcwd(), "uploads", file_name)
    # 检查文件是否存在
    if os.path.exists(file_path):
        # 操作数据库,记录最近下载时间和次数
        file_down = await File.get_or_none(file_name=file_name)
        file_down.download_count += 1
        await file_down.save()
        # 返回 FileResponse 对象
        return FileResponse(file_path)
    else:
        return {"error": "File not found"}


@file_api.get('/getAllFilesInfo', response_model=Result)
async def get_all_files():
    try:
        # 发起异步请求以获取所有文件信息
        files = await File().all()
        formatted_files = [
            {
                "file_id": file.file_id,
                "file_name": file.file_name,
                "upload_time": file.upload_time,
                "download_time": file.download_time,
                "download_count": file.download_count,
                "file_type": file.file_type,
                "file_size": file.file_size
            }
            for file in files]
        return Result(code=200, msg='Success', data=formatted_files)
    except:
        return Result(code=100, msg='获取文件信息错误!', data=[])
