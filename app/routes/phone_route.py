# FastAPI
from fastapi import APIRouter
from fastapi import Body

# Twilio
from twilio.rest import Client

# App
from app.config import env_vars
from app.schemas import phone_schema

client_twilio = Client(env_vars["twilio_username"], env_vars["twilio_password"])

router = APIRouter(
  prefix="/phone",
  tags=["Phone verification"]
)

@router.post(
  path="",
  summary="Get phone code verification"
)
def phone(phone: phone_schema.Phone = Body(...)):
  """
  Use country phone code and number phone to send a SMS to get a code verification

  Parameters:
  - Request body parameter:

    - **phone: Phone** -> A phone with country **code** and **number**
  
  Returns a message for successfull sended sms
  """
  verification = client_twilio.verify \
                        .services(env_vars["twilio_service_verification_id"]) \
                        .verifications \
                        .create(to=f"{phone.code}{phone.number}", channel="sms")
  print(verification)
  return { "msg": "Verification sended" }

@router.post(
  path="/verify",
  summary="Verify phone code received"
)
def phone_verify(verify: phone_schema.VerificationCode = Body(...)):
  """
  Use the code received to verify it

  Parameters:
  - Request body parameter:

    - **verify: VerificationCode** -> A **code** for verification and a **phone** number
  
  Returns a message for successfull verification code
  """
  check = client_twilio.verify \
                 .services(env_vars["twilio_service_verification_id"]) \
                 .verification_checks \
                 .create(to=verify.phone, code=verify.code)
  print(check)
  return { "data": { "valid": check.valid }, "msg": "Code validated" }
