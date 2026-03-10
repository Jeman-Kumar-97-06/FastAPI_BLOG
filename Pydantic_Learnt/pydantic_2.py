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
print(user1.username)

# user1.bio=300
# print(user1) #This works even if the bio is set to 'str'

user1.bio = 'Jack Ripper'

print(user1.model_dump()) #Prints the 'user1' model as dict
print(user1.model_dump_json()) # prints the 'user1' model as json

try:
    user2 = User(username='jeman',email=10,age="300",) 
except ValidationError as e:
    print(e)
'''
Only "email" will get validation error not the 'age' 
cuz python can turn integer to string if it has numeric value (a string of alphabets will give error though)
 but integer can't be turned into string 
'''

