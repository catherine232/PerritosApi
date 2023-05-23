from fastapi import FastAPI 

app=FastAPI()

@app.get("/")
def index():
    return "Hola a todos, quieres saber de perritos"
@app.get("/Perrito")
def perrito():
    return "Este es otro mensaje"
