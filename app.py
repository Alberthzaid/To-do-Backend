from flask import Flask
from Controllers.TaskControllers import getTask


app = Flask(__name__)


#Endpoint para traer todas las tareas  http://127.0.0.1:5000/task
@app.route('/task', methods=["GET"])
def getTasksRoute():
    return getTask()


if __name__ == '__main__':
    app.run()
