from fastapi import FastAPI, Form, Request
import uvicorn
from starlette.responses import HTMLResponse, RedirectResponse
from fastapi.params import Form
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from pydantic.main import BaseModel
from day14.daomember import DaoMember

templates = Jinja2Templates(directory="templates")
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


class MEM(BaseModel):
    m_id: str = None
    m_name: str= None
    tel: str= None
    email: str= None


@app.get("/", response_class=HTMLResponse)
async def root(request:Request):
    return RedirectResponse(url="/static/member.html")


@app.post("/mem_select")
def mem_select():
    dm = DaoMember()
    list = dm.selectList()
    return {"list": list}

@app.post("/mem_select_one")
def mem_select_one(m: MEM):
    dm = DaoMember()
    mem = dm.selectOne(m.m_id)
    return {"mem": mem}

@app.post("/mem_insert")
def mem_insert(m: MEM):
    dm = DaoMember()
    cnt = dm.insert(m.m_name, m.tel, m.email)
    return {"cnt": cnt}

@app.post("/mem_mod")
def mem_mod(m: MEM):
    dm = DaoMember()
    cnt = dm.update(m.m_id, m.m_name, m.tel, m.email)
    return {"cnt": cnt}

@app.post("/mem_del")
def mem_del(m: MEM):
    dm = DaoMember()
    cnt = dm.delete(m.m_id)
    return {"cnt": cnt}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
 