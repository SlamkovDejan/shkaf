import os

AUTH_SECRET = os.getenv("AUTH_SECRET", "SECRET")

DATABASE_USER = os.getenv("DATABASE_USER", "postgres")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "password")
DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_PORT = os.getenv("DATABASE_PORT", "5434")
DATABASE_NAME = os.getenv("DATABASE_NAME", "shkafdb")
