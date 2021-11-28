from fastapi import FastAPI
from routers import animal

app = FastAPI(
    title="AnimaPet",
    description="API AnimaPet",
    version="0.0.1",
)

@app.get("/")
def root():
    return {"msg": "AnimaPet"}

app.include_router(
    animal.router,
    responses={404: {"description": "Not found"}},
)

