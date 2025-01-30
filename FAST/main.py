from fastapi import FastAPI
from typing import Optional

app = FastAPI(
    title='Mi primer API 192',
    description='Roberto Uriel Martinez Martinez',
    version='1.0.1'
)

usuarios = [
    {"id": 1, "nombre": "Uriel", "edad": 20},
    {"id": 2, "nombre": "Isay", "edad": 37},
    {"id": 3, "nombre": "Evel", "edad": 20},
    {"id": 4, "nombre": "Ana", "edad": 18}
]

# Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello': 'world FastAPI'}

# Endpoint promedio
@app.get('/promedio', tags=['Promedios'])
def promedio():
    return 5.5

# Endpoint parámetro obligatorio
@app.get('/usuario/{id}', tags=['Parámetro obligatorio'])
def consultaUsuario(id: int):
    # conectamos a la BD
    # consultamos
    return {'Se encontró el usuario': id}

# Endpoint parámetro opcional
@app.get('/usuario/', tags=['Parámetro Opcional'])
def consultaUsuario2(id: Optional[int] = None):
    if id is not None:
        for usu in usuarios:
            if usu["id"] == id:
                return {"mensaje": "Usuario encontrado", "usuario": usu}
        return {"mensaje": f"No se encontró el usuario con id: {id}"}
    else:
        return {"mensaje": "No se proporcionó un id"}