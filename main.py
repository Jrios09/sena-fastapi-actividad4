
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List, Union


app = FastAPI()

class Producto(BaseModel):
    nombre: str
    precio: float
    en_stock: bool
    tags: Optional[List[str]] = None


class Orden(BaseModel):
    cliente: str
    items: List[str]

class Respuesta(BaseModel):
    valor:Union[str,int]

class Perfil(BaseModel):
    usuario: str
    bio: Optional[str] = None
    intereses: Optional[List[str]] = None

class Calificacion(BaseModel):
    curso: str
    nota: float

class Config(BaseModel):
    modo:str = "produccion"
    version: float = 1.0

class Estricto(BaseModel):
    cantidad: int

@app.get("/")
def hola_mundo():
    return {"mensaje": "Bienvenidos a nuestra API"}

@app.post("/productos/")
def crear_producto(producto: Producto):
    return {
        "mensaje": f"Producto {producto.nombre} creado correctamente",
        "eco": producto  # Eco de datos válidos (como indica la tabla)
    }

@app.get("/productos/buscar/")
def buscar_producto(nombre: str, categoria: Optional[str] = None):
    return {"nombre": nombre, "categoria": categoria}

@app.post("/orden/")
def crear_orden(orden: Orden):
    return {"total_items": len(orden.items), "cliente": orden.cliente}

@app.post("/respuesta/")
def crear_respuesta(respuesta: Respuesta):
    return {"tipo": type(respuesta.valor).__name__, "valor": respuesta.valor}

@app.post("/perfil/")
def crear_perfil(perfil: Perfil):
    return {
        "usuario": perfil.usuario,
        "bio": perfil.bio,
        "intereses": perfil.intereses
    }

@app.post("/calificacion/")
def crear_calificacion(calificacion: Calificacion):
    return {
        "curso": calificacion.curso,
        "nota": calificacion.nota
    }

@app.post("/configuracion/")
def crear_config(config: Config):
    return {
        "mensaje": "Configuración recibida correctamente",
        "modo": config.modo,
        "version": config.version
    }

@app.post("/validacion/estricta")
def validar_estricto(dato: Estricto):
    return {"mensaje": f"Cantidad válida: {dato.cantidad}"}