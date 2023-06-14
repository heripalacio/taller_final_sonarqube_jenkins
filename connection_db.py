from pymongo import MongoClient

def collection_db():
    client = MongoClient("mongodb://localhost:27017/")
    database = client["ddp_pruebas"]

    collection_name = "pruebas_collection"
    collection = database[collection_name]

    return collection