from fastapi import FastAPI

from routers import animal, usuario

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

app.include_router(
    usuario.router,
    responses={404: {"description": "Not found"}},
)

