from fastapi import FastAPI, Form, Request
import uvicorn
from starlette.responses import HTMLResponse, RedirectResponse
from fastapi.params import Form
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from pydantic.main import BaseModel
from day13.daoemp import DaoEmp

templates = Jinja2Templates(directory="templates")
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class Item(BaseModel):
    e_id: str

class EMP(BaseModel):
    e_id: str = None
    e_name: str= None
    gen: str= None
    addr: str= None


@app.get("/", response_class=HTMLResponse)
async def root(request:Request):
    return RedirectResponse(url="/static/emp.html")


@app.post("/myajax")
def myajax(item: Item):
    print(item.e_id)
    return {"e_id": "맛있다"}

@app.post("/emp_select")
def emp_select():
    de = DaoEmp()
    list = de.selectList()
    return {"list": list}

@app.post("/emp_select_one")
def emp_select_one(e: EMP):
    de = DaoEmp()
    emp = de.selectOne(e.e_id)
    return {"emp": emp}

@app.post("/emp_insert")
def emp_insert(e: EMP):
    de = DaoEmp()
    cnt = de.insert(e.e_id, e.e_name, e.gen, e.addr)
    return {"cnt": cnt}

@app.post("/emp_mod")
def emp_mod(e: EMP):
    de = DaoEmp()
    cnt = de.update(e.e_id, e.e_name, e.gen, e.addr)
    return {"cnt": cnt}

@app.post("/emp_del")
def emp_del(e: EMP):
    de = DaoEmp()
    cnt = de.delete(e.e_id)
    return {"cnt": cnt}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
 