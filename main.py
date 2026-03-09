from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
#jinja2 is inlcluded in fastapi
from fastapi.templating import Jinja2Templates

from fastapi.staticfiles import StaticFiles

#intialize an app
app = FastAPI()

'''
First  Arg : url of the location of 'static' folder.
Second Arg : StaticFiles instance pointing to 'static' folder.
Third  Arg : "name" says the folder is accessible at 'static' 
'''
app.mount("/static",StaticFiles(directory="static"),name='static')

#Tell this app, where to find the Jinja2 templates:
templates = Jinja2Templates(directory='templates')

#Mock up Data:
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

@app.get('/api/posts')
def get_posts():
    return posts


#The following 2 routes will do the same shit:
@app.get('/api/posts_length', response_class=HTMLResponse)
@app.get('/api/posts_len',response_class=HTMLResponse)
def get_fancy():
    return f"<h1>{len(posts)}</h1>"

#This will work, but you won't be able to see this in the '/docs' or '/redoc'
@app.get("/api/shit_route",include_in_schema=False)
def get_shit():
    return f"<h1>Pathetic Route</h1>"

#SERIOUS SHIT --------------------------------------------------------------------------------------

@app.get('/api/all_posts')
def posts_home(request: Request):
    return templates.TemplateResponse(request,'home.html',{"posts":posts,"title":"Posts_Home"})

@app.get('/api/about',name='about') # Now, the url_for should be 'about' not 'about_page'
def about_page(request: Request):
    return templates.TemplateResponse(request,'about.html',{"title":"About_Page"})

#route to get a specific post
@app.get('/api/posts/{post_id}')
def get_post(post_id:int):
    for post in posts:
        if post.get('id') == post_id:
            return post
    return {"error":"NO Post with the post_id"}

#---------------------------------------------------------------------------------------------------