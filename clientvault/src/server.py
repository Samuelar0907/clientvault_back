from sched import scheduler
from fastapi import FastAPI
from contextlib import asynccontextmanager
# from .routes import feedback, managers, feedbackarea_manager
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("starting scheduler")
    scheduler.start()
    yield


app = FastAPI(lifespan=lifespan)



# app.include_router(feedback.router)
# app.include_router(managers.router)
# app.include_router(feedbackarea_manager.router)

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