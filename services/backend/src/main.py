from fastapi import FastAPI
from tortoise import Tortoise  # NEW

from src.database.register import register_tortoise  # NEW
from src.database.config import TORTOISE_ORM    


Tortoise.init_models(["src.database.models"], "models") 

from src.routes import users,notes

app = FastAPI()
app.include_router(users.router)
app.include_router(notes.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

@app.get("/")
def home():
    return "Hello,World!"

    