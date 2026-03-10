from pydantic import BaseModel, ValidationError,Field
from datetime import datetime, UTC
from typing import Literal, Annotated

class BlogPost(BaseModel):
    title: str 
    content: str
    view_count: int = 0
    is_published: bool = False
    tags: list[str] = Field(default_factory=list)# --> tags is going to be a list of strings
    #default_factory says "when creating new objects call this fuction to generate the default value of 'list'"
    #it creates a unique list for each object.
    #Ex: Without 'Field' and 'default_factory':
    '''
        class BadModel(BaseModel):
            tags: list[str] = []

        a = BadModel()
        b = BadModel()

        a.tags.append("python")

        print(b.tags) --> ['python']
        print(a.tags) --> ['python']
    '''
    create_at: datetime = Field(default_factory = lambda: datetime.now(tz=UTC))
    author_id: str|int 
    username:Annotated[str,Field(min_length=3,max_legnth=20)]
    status: Literal['draft','published','archived'] = 'draft'


post = BlogPost(
    title = "Getting started with Python",
    content = "Here's how to begin...",
    author_id='12345'
)