"""
Created on 2024/3/21 09:37 
Author: Shuijing
Description: 
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE_PATH = os.path.join(BASE_DIR, 'FlashTrans.db')  # 不需要提前创建数据库,直接这里填写即可
TORTOISE_ORM = {
    "connections": {"default": f"sqlite:///{DB_FILE_PATH}"},
    "apps": {
        "models": {
            "models": [
                "db.models.UserModel",
                'db.models.FileModel',
                "aerich.models"
            ],  # 生成的时候不要加DB，等项目启动的时候再加db,注意要将所有的model写进去

            "default_connection": "default",
        },
    },
}
