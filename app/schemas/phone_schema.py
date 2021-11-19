# FastAPI (Pydantic)
from pydantic import BaseModel, Field

# App
from app.config import env_vars

class Phone(BaseModel):
  code: str = Field(..., min_length=1, max_length=6, example=env_vars["phone_model_code_example"])
  number: str = Field(..., min_length=1, max_length=15, example=env_vars["phone_model_number_example"])

class VerificationCode(BaseModel):
  code: str = Field(..., min_length=6, max_length=6)
  phone: str = Field(..., min_length=12, max_length=25)