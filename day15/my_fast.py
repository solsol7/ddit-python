from fastapi import FastAPI, Form, Request
import uvicorn
from starlette.responses import HTMLResponse, RedirectResponse
from fastapi.params import Form
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from pydantic.main import BaseModel
from day13.daoemp import DaoEmp
from day15.daoexam import DaoExam

templates = Jinja2Templates(directory="templates")
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class EXAM(BaseModel):
    e_id: str = None
    m_id: str= None
    kor: str= None
    eng: str= None
    math: str= None


@app.get("/", response_class=HTMLResponse)
async def root(request:Request):
    return RedirectResponse(url="/static/exam.html")


@app.post("/exam_select")
def exam_select():
    de = DaoExam()
    list = de.selectList()
    return {"list": list}


@app.post("/exam_select_one")
def exam_select_one(e: EXAM):
    de = DaoExam()
    exam = de.selectOne(e.e_id)
    return {"exam": exam}


@app.post("/exam_insert")
def exam_insert(e: EXAM):
    de = DaoExam()
    cnt = de.insert(e.m_id, e.kor, e.eng, e.math)
    return {"cnt": cnt}

@app.post("/exam_mod")
def exam_mod(e: EXAM):
    de = DaoExam()
    cnt = de.update(e.e_id, e.m_id, e.kor, e.eng, e.math)
    return {"cnt": cnt}

@app.post("/exam_del")
def emp_del(e: EXAM):
    de = DaoExam()
    cnt = de.delete(e.e_id)
    return {"cnt": cnt}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
 