# App
from app.libs.models import user_model, item_model
from app.libs import database
from app.routes import main

# FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

user_model.Base.metadata.create_all(bind=database.engine)
item_model.Base.metadata.create_all(bind=database.engine)

origins = [
  "*"
]

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(main.routes_v1)

@app.get("/", tags=["Others"])
def home():
  return { "hello": "world" }
