import uvicorn
from fastapi import FastAPI
from routers.users.user import users


app = FastAPI()

app.include_router(users, tags=["用户信息"], prefix="/user")


if __name__ == "__main__":
    uvicorn.run("main:app", host="110.41.67.159", port=8080, reload=True, )