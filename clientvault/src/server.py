#from sched import scheduler
#from contextlib import asynccontextmanager
from fastapi import FastAPI
from .routes import test
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() #lifespan=lifespan

app.include_router(test.router)

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