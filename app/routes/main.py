from fastapi import APIRouter

from app.routes import user_route, auth_route, phone_route

routes_v1 = APIRouter(
  prefix="/api/v1",
  tags=["API V1"]
)

routes_v1.include_router(user_route.router)
routes_v1.include_router(auth_route.router)
routes_v1.include_router(phone_route.router)
