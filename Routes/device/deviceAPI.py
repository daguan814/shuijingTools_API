"""
Created on 2024/4/11 18:14 
Author: Shuijing
Description: 
"""
from datetime import datetime

from fastapi import APIRouter
from pydantic import BaseModel

from db.models.DeviceModel import Device
from tools.ResultResponse import Result

device = APIRouter()


class deviceIn(BaseModel):
    device_name: str
    another_info: str
    address_mac: str
    address_ip: str


# 报告班级信息
@device.post('/report', response_model=Result)
async def create_device(device_in: deviceIn):
    # 查询该设备是否存在，如果存在则更新信息，否则创建新对象
    print(device_in)
    device_ob = await Device.get_or_none(device_name=device_in.device_name)
    if device_ob is not None:
        # 如果是新创建的对象，则设置 first_send_time 字段
        # 更新或设置其他字段
        device_ob.another_info = device_in.another_info
        device_ob.address_mac = device_in.address_mac
        device_ob.address_ip = device_in.address_ip
        # 保存对象
        await device_ob.save()
        return Result(code=100, msg='更新班级信息成功', data=[{}])
    else:
        device_ob = Device(
            device_name=device_in.device_name,
            another_info=device_in.another_info,
            address_mac=device_in.address_mac,
            address_ip=device_in.address_ip
        )
        await device_ob.save()
        return Result(code=200, msg='新建记录成功', data=[{}])
