from fastapi import FastAPI, Body
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

class UserIn(BaseModel):
    name: str 
    age: int 
    gender: str = Field(max=100)

@app.get("/")
async def root():
    return {'message': 'Welcome'}

@app.post("/user")
async def get_users(user: UserIn,q: int):
    return {'name': user.name, 'q': q}

@app.get("/user/{user_id}")
async def get_users(user_id: int):
    return {'message': f'Selected user id {user_id}'}
