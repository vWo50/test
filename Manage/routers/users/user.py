from fastapi import APIRouter
from fastapi import Form

users = APIRouter()  # 主要先实现人员的增删改查


@users.post("/")
async def login():
    return{
        "message": "登陆成功！"
    }
