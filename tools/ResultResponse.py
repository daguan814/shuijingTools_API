"""
Created on 2024/3/21 09:42 
Author: Shuijing
Description: 
"""
from typing import List, Dict, Any

from pydantic import BaseModel


class Result(BaseModel):
    code: int
    msg: str
    data: List[Dict[str, Any]]
