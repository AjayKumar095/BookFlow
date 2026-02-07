import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


## Database configuration

class Config:
    SQL_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "database.db")
    SQL_TRACK_MODIFICATIONS = False