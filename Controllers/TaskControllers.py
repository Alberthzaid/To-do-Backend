from flask import jsonify , request

from bson import ObjectId
from Config.Index import DataBase

#Hola Gabriel... Esta intenta entender este codigo y aplica mas consultas para la base de datos

# Función para convertir ObjectId a string en documentos anidados
def convert_objectid_to_str(doc):
    for key, value in doc.items():
        if isinstance(value, ObjectId):
            doc[key] = str(value)
        elif isinstance(value, dict):
            convert_objectid_to_str(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    convert_objectid_to_str(item)
    return doc

def getTask():
    task_collection = DataBase['Task']
    tasks = list(task_collection.find())  # Convertir el cursor a una lista de diccionarios
    
    # Convertir todos los ObjectId a strings
    tasks = [convert_objectid_to_str(task) for task in tasks]
    
    return jsonify(tasks)
# Devolver la lista en formato JSON

# insertar una nueva tarea

def addTask():
    task_collection = DataBase['Task']
    new_task = request.json  # Recibe la tarea desde el cliente como JSON
    inserted = task_collection.insert_one(new_task)  # Inserta en la base de datos
    new_task["_id"] = str(inserted.inserted_id)  # Convierte el ObjectId a string
    return jsonify(new_task), 201  # Devuelve la tarea insertada con el código HTTP 201
