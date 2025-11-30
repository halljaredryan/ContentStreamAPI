from pydantic import BaseModel

#used to recieve body data
class PostCreate(BaseModel):
    title:str
    content: str

class PostResponse(BaseModel):
    title:str
    content: str