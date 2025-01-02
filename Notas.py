from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import date

# Definindo o modelo de Nota
class Nota(BaseModel):
    nome: str
    nota: float
    disciplina: str
    data: date


notas_list = []

app = FastAPI()


@app.post("/notas/", response_model=Nota)
async def criar_notas(nota: Nota):
    id_nota = len(notas_list) + 1
    nota_dict = nota()  
    nota_dict["id"] = id_nota 
    notas_list.append(nota_dict)  
    return nota_dict  

# Endpoint para obter todas as notas
@app.get("/notas/", response_model=List[Nota])
async def obter_notas():
    return notas_list
