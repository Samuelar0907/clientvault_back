from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import client_potential

app = FastAPI() #lifespan=lifespan

app.include_router(client_potential.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solo el origen necesario
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=['root'])
async def root():
    return {"message": "Hello Bigger Applications!"}