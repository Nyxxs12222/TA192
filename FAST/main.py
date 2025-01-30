from fastapi import FastAPI

app= FastAPI(
    title = 'Mi primerAPI 192',
    description = 'Rberto Uriel Martinez Martinez',
    version = '1.0.1'
)

#Endpoint home 
@app.get('/', tags = ['Hola Mundo'])
def home():
    return {'hello':'wordl FastAPI'}

#Endpoint promedio 
@app.get('/promedio', tags = ['Promedios'])
def promedio():
    return 5.5

#Endpoint parametro Obligactorio 
@app.get('/usuario/{id}', tags = ['Parametro obligatorio'])
def consultaUsuario(id:int):
    #conectamos a la BD
    #consultamos
    return {'Se encontro el usuario':id}