# Python
from os import environ
from dotenv import load_dotenv

load_dotenv()

env_vars = {
  "twilio_username": environ.get("TWILIO_USERNAME"),
  "twilio_password": environ.get("TWILIO_PASSWORD"),
  "twilio_service_verification_id": environ.get("TWILIO_SERVICE_VERIFICATION_ID"),
  "phone_model_code_example": environ.get("PHONE_MODEL_CODE_EXAMPLE"),
  "phone_model_number_example": environ.get("PHONE_MODEL_NUMBER_EXAMPLE"),
  "db_user": environ.get("DB_USER"),
  "db_password": environ.get("DB_PASSWORD"),
  "db_host": environ.get("DB_HOST"),
  "db_port": environ.get("DB_PORT"),
  "db_name": environ.get("DB_NAME")
}