import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# --- On cloud resources ---
# Mongo configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Redis configuration
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")