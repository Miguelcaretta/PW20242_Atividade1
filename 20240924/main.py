from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn

from util import ler_html, salvar_cadastro, salvar_contato
from repositories import_repo
import usuario_repo as usuario
app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/sobre")
def get_sobre(request: Request):
    return templates.TemplateResponse("sobre.html", {"request": request})

@app.get("/contato")
def get_contato(request: Request):
    return templates.TemplateResponse("contato.html", {"request": request})

@app.post("/post_contato")
def post_contato(
    request: Request, 
    nome: str = Form(...), 
    email: str = Form(...), 
    assunto: str = Form(...), 
    mensagem: str = Form(...)):
    salvar_contato(nome, email, assunto, mensagem)
    return RedirectResponse("/contato_recebido", 303)

@app.get("/contato_recebido")
def get_contato_recebido(request: Request):
    return templates.TemplateResponse("contato_recebido.html",{"request": request})

@app.get("/cadastro")
def get_cadastro(request: Request):
   return templates.TemplateResponse("cadastro.html",{"request": request})

@app.post("/post_cadastro")
def post_cadastro(
    nome: str = Form(...), 
    data_nascimento: str = Form(...), 
    telefone: str = Form(...), 
    email: str = Form(...), 
    senha: str = Form(...), 
    confirmacao_senha: str = Form(...)):
    if senha == confirmacao_senha:
        usuario.inserir () _cadastro(nome, data_nascimento, email, senha)
        return RedirectResponse("/cadastro_recebido", 303)
    else:
        return RedirectResponse("/cadastro", 303)

@app.get("/cadastro_recebido")
def get_cadastro_recebido(request: Request):
    html = ler_html("cadastro_recebido")
    return HTMLResponse(html)

@app.get("/entrar")
def get_contato(request: Request):
   return templates.TemplatesResponse("entrar.html", {"request": request})

if name == "main":
    uvicorn.run("main:app", port=8000, reload=True)