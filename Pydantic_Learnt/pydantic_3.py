from pydantic import BaseModel, ValidationError,Field
from datetime import datetime

class BlogPost(BaseModel):
    title: str 
    content: str
    view_count: int = 0
    is_published: bool = False

    tags: list[str] = Field(default_factory=list)# --> tags is going to be a list of strings