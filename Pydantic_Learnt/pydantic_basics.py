from pydantic import BaseModel

#Pydantic is used for data validation.
#Ex1: Without using pydantic:
def create_user(username, email, age):
    if not isinstance(username, str):
        raise TypeError("Username must be a string!")
    if not isinstance(email, str):
        raise TypeError("Invalid email format")
    if not isinstance(age, int):
        raise TypeError("Age must be an Integer")
    
    return {"username":username, "email":email, "age":age}

user1 = create_user('jeman','jk@gmail.com',39)
print(user1)
print("*"*50)
# user2 = create_user('jack',None,'old')
# print(user2) -------------> This will give error

#Ex2: Using pydantic:
class User(BaseModel):
    username: str
    email: str
    age: int

user1 = User(username='jeman',email='jk@gmail.com',age=30)
print(user1)

user2 = User(username='jack', email=None, age='old')
print(user2)