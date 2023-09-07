from fastapi import FastAPI, Form, Request
import uvicorn
from starlette.responses import HTMLResponse
from fastapi.params import Form
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root():
    return "Hello World"

@app.get("/param", response_class=HTMLResponse)
async def param(menu: str):
    return "param"+menu

@app.post("/post", response_class=HTMLResponse)
async def post(menu: str=Form()):
    return "post:"+menu

@app.get("/forw")
async def forw(request: Request):
    a = '홍길동'
    b = ['베어그릴스','솔로지옥','정글의법칙']
    c = [
        {'e_id': 1, 'e_name': '1', 'gen': '1', 'addr': '1'},
        {'e_id': 2, 'e_name': '2', 'gen': '2', 'addr': '2'}
        ]
    return templates.TemplateResponse('forw.html', {'request':request, "a": a, "b": b, "c": c})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
