from dotenv import load_dotenv
import os


class Config:
    def __init__(self):
        load_dotenv("../.env")
        print(os.getcwd())
        self.tg_token = os.environ.get("tg_token")
        self.host = os.environ.get("HOST")
        self.port = os.environ.get("PORT")
