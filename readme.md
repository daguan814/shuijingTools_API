

pip install tortoise-orm
pip install aerich


先进入db文件夹
初始化生成
aerich init -t settings.TORTOISE_ORM
生成数据库
aerich init-db

aerich migrate 迁移
aerich upgrade 更新

回退
aerich downgrade
