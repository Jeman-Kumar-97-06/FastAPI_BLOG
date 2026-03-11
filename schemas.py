from pydantic import BaseModel, ConfigDict, Field

class PostBase(BaseModel):
    title: str = Field(min_length=1,max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)

class PostCreate(PostBase):
    pass #We want title, content, author

class PostResponse(PostBase):
    #The following line inherits everything from the PostBase:
    '''
    Also, Posts are dicts. So to access the attributes, you use bracket notation.
    'from_attributes=True' makes us access using dot notation, like in objects. Bcoz the 
    shit from databases are received by pydantic as Objects.
    '''
    model_config = ConfigDict(from_attributes=True) 
    #Xtra shit we need from the response that aren't in the PostBase:
    id: int
    date_posted: str
