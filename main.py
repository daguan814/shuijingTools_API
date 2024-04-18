import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from Routes.device.deviceAPI import device
from Routes.file.fileAPI import file_api
from Routes.log.logAPI import log
from Routes.net.netAPI import net
from Routes.version.versionAPI import version
from db.settings import TORTOISE_ORM
from tools.download.download import download


app = FastAPI()

app.include_router(file_api, prefix='/file', tags=['文件管理'])
app.include_router(device, prefix='/device', tags=['设备管理'])
app.include_router(log, prefix='/log', tags=['日志添加'])
app.include_router(net, prefix='/net', tags=['网络检查'])
app.include_router(version, prefix='/version', tags=['版本检查'])

# 注册和配置ORM的组件 main一运行，
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
