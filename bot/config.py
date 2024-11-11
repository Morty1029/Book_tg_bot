from dotenv import load_dotenv
import os


class Config:
    def __init__(self):
        load_dotenv("../.env")
        self.tg_token = os.environ.get("tg_token")
