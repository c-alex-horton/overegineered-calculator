from fastapi import FastAPI

from .routers import maths

app = FastAPI()

app.include_router(maths.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# run with 'uvicorn app.main:app --reload' in parent dir
