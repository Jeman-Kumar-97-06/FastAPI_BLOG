from pydantic import BaseModel, ValidationError
from datetime import datetime

class User(BaseModel):
    username: str
    email: str
    age: int
    bio: str = "" #Default is empty string
    is_active: bool = True #Default is True
    fullname: str | None = None  # it's "string UNION none" but the default is "None"
    verified_at: datetime | None = None

user1 = User(username='jeman',email='jk@gmail.com',age=30)

