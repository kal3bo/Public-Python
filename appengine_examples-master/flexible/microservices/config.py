import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Auth0
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")