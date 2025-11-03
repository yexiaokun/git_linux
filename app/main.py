from fastapi import FastAPI
app = FastAPI(title="Hello FastAPI")

@app.get("/")
def read_root():
    return {"message":"欢迎来到fastapi"}

@app.get("/user/{name}")
def greet_user(name: str):
    return {"message":f"你好，{name}!FastAPI好用吗？"}

@app.get("/user/{user_id}")
def get_user_id(user_id: int):
    return {"message":f"你好，你的id是{user_id}!"}