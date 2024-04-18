"""
Created on 2024/4/16 14:20 
Author: Shuijing
Description: 
"""
import os


def get_file_size(file_path):
    try:
        # 获取文件大小（以字节为单位）
        size_in_bytes = os.path.getsize(file_path)

        # 将字节转换为 MB
        size_in_mb = size_in_bytes / (1024 * 1024)

        return size_in_mb
    except Exception as e:
        print("获取文件大小失败:", e)
        return None