# SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# App
from app.config import env_vars

# SQLALCHEMY_DATABSE_URL = f'mysql+pymysql://{env_vars["db_user"]}:{env_vars["db_password"]}@{env_vars["db_host"]}:{env_vars["db_port"]}/{env_vars["db_name"]}'
SQLALCHEMY_DATABSE_URL = "mysql+pymysql://{}:{}@{}:{}/{}".format(
  env_vars["db_user"],
  env_vars["db_password"],
  env_vars["db_host"],
  env_vars["db_port"],
  env_vars["db_name"]
)

engine = create_engine(SQLALCHEMY_DATABSE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()