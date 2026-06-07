from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional

class Post(BaseModel):
    title:str
    content:str
    
    
class Post_get(BaseModel):
    id:int 
    title:str
    content:str
    created_at:datetime
    owner_id:int
    owner:UserOut

class Post_post(BaseModel):
    title:str
    content:str
    owner_id:int

    class Config:
        from_attributes=True

class PostOut(BaseModel):
    Post : Post_get
    votes : int

    class Config:
        from_attributes=True

class UserCreate(BaseModel):
    email_id:EmailStr
    password:str

class UserOut(BaseModel):
    id:int
    email_id:EmailStr
    created_at:datetime

    class Config:
        from_attributes=True

class UserLogin(BaseModel):
    email_id : EmailStr
    password : str

class Token(BaseModel):
    token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[int]

class Vote(BaseModel):
    post_id : int
    dir : int
    