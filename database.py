import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Cargar variables de entorno
load_dotenv()

# Conectar a MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client["UNIVERSITYSP"]

def get_collection(collection_name):
    return db[collection_name]

