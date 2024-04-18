"""
Created on 2024/4/16 09:19 
Author: Shuijing
Description: 
"""
from db.models.RunLogModel import RunLog
from tools.ResultResponse import Result
from fastapi import APIRouter
from pydantic import BaseModel

log = APIRouter()


class RunLogIn(BaseModel):
    device_name: str
    log_type: str
    log_message: str


@log.post('/logAdd', response_model=Result)
async def create_device(runlog_in: RunLogIn):
    run_log = RunLog(
        device_name=runlog_in.device_name,
        log_type=runlog_in.log_type,
        log_message=runlog_in.log_message
    )
    await run_log.save()
    return Result(code=200, msg='日志记录成功', data=[{}])
