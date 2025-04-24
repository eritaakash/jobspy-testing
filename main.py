from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from utils.job_scrape import get_jobs 
import pandas as pd 

app = FastAPI()

# Mount static files like CSS, JS
app.mount('/static', StaticFiles(directory='static'), name='static')

# Use templates from templates folder
templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
async def serve_home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.get('/api/jobs')
async def say_hello():
    res = get_jobs()
    
    if res['ready']:
        return {'data': res['data']}

    else:
        return {'error': res['error']}
    