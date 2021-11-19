# SQLAlchemy
from sqlalchemy.orm import Session

# FastAPI
from fastapi import APIRouter, HTTPException, status
from fastapi import Body, Path, Depends

# App
from app.schemas import user_schema
from app.services import user_service
from app.dependencies import get_db

router = APIRouter(
  prefix="/auth",
  tags=["Auth"]
)

@router.post(
  path="/signup",
  response_model=user_schema.User,
  status_code=status.HTTP_201_CREATED,
  summary="Register a user"
)
def signup(user: user_schema.UserCreate = Body(...), db: Session = Depends(get_db)):
  """
  Parameters:
    - Request body parameter
      - user: UserCreate

  Returns a json with the basic user information:
    - user_id: UUID
    - email: EmailStr
    - first_name: str
  """
  db_user = user_service.get_user_by_email(db, email=user.email)
  if db_user:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
  return user_service.create_user(db=db, user=user)

@router.post(
  path="/signin",
  response_model=user_schema.User,
  status_code=status.HTTP_200_OK,
  summary="Login a user"
)
def signin(user: user_schema.UserCreate = Body(...)):
  if user.email != "tonalli@example.com":
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="This user doesn't exist"
    )
  return user