from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from pydantic import ConfigDict

class Post(BaseModel):
    title:str
    content:str
    
class UserOut(BaseModel):
    id:int
    email_id:EmailStr
    created_at:datetime

    model_config = ConfigDict(
        from_attributes=True
    )
    
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

    

class PostOut(BaseModel):
    Post : Post_get
    votes : int

    model_config = ConfigDict(
        from_attributes=True
    )

class UserCreate(BaseModel):
    email_id:EmailStr
    password:str



class UserLogin(BaseModel):
    email_id : EmailStr
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[int]

class Vote(BaseModel):
    post_id : int
    dir : int
    