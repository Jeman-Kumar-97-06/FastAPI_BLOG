from fastapi import FastAPI

#intialize an app
app = FastAPI()

posts : list[dict] = [
    {
        "id":1,
        "author":"Corey Schafer",
        "title":"FastAPI is Awesome",
        "content":"This framework is really easy to use and super fast.",
        "date_posted":"April 20, 2025"
    },
    {
        "id":2,
        "author":"Jane Doe",
        "title":"Python is Great for Web Development",
        "content":"Python is great for web development, and FastAPI makes it even better",
        "date_posted":"April 21, 2025"
    },
]

@app.get("/")
def home():
    return {'message':"Hello World Jeman!"}

