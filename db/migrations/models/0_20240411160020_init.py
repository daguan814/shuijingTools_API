from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "device" (
    "device_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL /* 设备id */,
    "device_name" VARCHAR(50) NOT NULL  /* 设备名 */,
    "another_info" VARCHAR(200) NOT NULL  /* 其余说明 */,
    "address_mac" VARCHAR(40) NOT NULL  /* mac地址 */,
    "address_ip" TIMESTAMP NOT NULL  /* ip地址 */,
    "first_send_time" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP /* 第一次报告时间 */
);
CREATE TABLE IF NOT EXISTS "file" (
    "file_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL /* 文件id */,
    "file_name" VARCHAR(50) NOT NULL  /* 文件名 */,
    "upload_time" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP /* 上传时间 */,
    "download_time" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP /* 最后一次下载的时间 */,
    "download_count" INT NOT NULL  DEFAULT 0 /* 下载次数 */,
    "file_type" VARCHAR(20) NOT NULL  /* 文件类型,安装包或者压缩包 */,
    "file_size" VARCHAR(20) NOT NULL  /* 文件大小,以MB为单位 */
);
CREATE TABLE IF NOT EXISTS "runlog" (
    "log_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL /* 日志id */,
    "device_name" VARCHAR(50) NOT NULL  /* 设备名 */,
    "log_time" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP /* 日志产生时间 */,
    "log_type" VARCHAR(50) NOT NULL  /* 日志重要程度 */,
    "log_message" VARCHAR(200) NOT NULL  /* 日志信息 */
);
CREATE TABLE IF NOT EXISTS "version" (
    "version_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL /* 版本id,主要是知道是第几次更新版本 */,
    "version_name" VARCHAR(50) NOT NULL  /* 版本名 */
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
