import sqlalchemy
import os
import dotenv

dotenv.load_dotenv()

# Cargamos todas las claves de configuracion guardadas en el archivo .env
class Settings():
    DB_NAME = os.getenv('DB_NAME')
    DB_HOST = os.getenv('DB_HOST')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_PORT = os.getenv('DB_PORT', 5432)
    SECRET_KEY = os.getenv("SECRET_KEY")  
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

settings = Settings()