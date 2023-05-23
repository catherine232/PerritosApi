from fastapi import FastAPI 

app=FastAPI()

@app.get("/")
def index():
    return "Hola a todos, quieres saber de perritos"
@app.get("/Perrito/{num}")
def perrito(num):
    return num 
@app.get("/Conversor_CaF/{C}")
def conversorCaF(C):
    try:
        
            C=float(C)
            TF=C*(9/5) + 32
            return f"La temperatura es de {TF} grados Farenheit"
    except:
            return "Entrada invalida"

