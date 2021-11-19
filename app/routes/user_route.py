# FastAPI
from fastapi import APIRouter
from fastapi import Path, Depends

# App
from app.dependencies import get_token_header

router = APIRouter(
  prefix="/users",
  tags=["Users"]
  # dependencies=[Depends(get_token_header)]
)

@router.get("")
async def read_users():
  return [{ "username": "Rick" }, { "username": "Morty" }]

@router.get("/me")
async def read_user_me():
  return { "username": "fakecurrentuser" }

@router.get("/{username}")
async def read_user(username: str = Path(...)):
  return { "username": username }