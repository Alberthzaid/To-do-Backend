import pymongo
import certifi

ca = certifi.where()

def connect(URI):
    try:
        client = pymongo.MongoClient(URI , tlsCaFile = ca)
        db = client["Todo-App"]
        print("Conexion exitosa")
        return db
    except ConnectionError:
        print("Algo ha salido mal ")
        print(ConnectionError)
