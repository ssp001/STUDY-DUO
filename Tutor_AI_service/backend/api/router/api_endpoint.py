from fastapi import FastAPI
from .. import api


app = FastAPI(name="fast api endpoint")
app.include_router(router=api.router, prefix="/api/v1")
