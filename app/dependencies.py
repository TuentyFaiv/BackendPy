# FastAPI
from fastapi import Header, HTTPException, status
from starlette.status import HTTP_400_BAD_REQUEST

# App
from app.libs.database import SessionLocal

async def get_token_header(x_token: str = Header(...)):
  if x_token != "fake-super-secret-token":
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="X-Token header invalid")

async def get_query_token(token: str):
  if token != "jessica":
    raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="No Jessica token provided")

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()