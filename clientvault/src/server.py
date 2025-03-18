from fastapi import FastAPI
from .routes import client
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() #lifespan=lifespan

app.include_router(client.router)


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