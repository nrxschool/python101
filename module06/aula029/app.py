import logging
import json
from flask import Flask, render_template, request
from task.task import Task
from database.db import ler_tarefas_do_arquivo, escrever_tarefas_no_arquivo
import signal
import sys

logging.basicConfig(level=logging.DEBUG)

### WEB SERVER
app = Flask(__name__)
tasks = ler_tarefas_do_arquivo("./database/db.txt")

### ROUTER TASK CRUD


## Create task
## POST /task {"description": "", "priority": 0, "completed": False }: id
@app.post("/task")
def add_task():
    data = json.loads(request.data)

    task = Task(data["description"], data["priority"], data["completed"])
    tasks[task.uuid.hex] = task
    return json.dumps({"uuid": task.uuid.hex})


## Read task
## GET /task/{id}: Task
@app.get("/task/<uuid>")
def get_a_task(uuid):
    # tratar KeyError
    return json.dumps(tasks[uuid].to_json())


## GET /tasks: List[Task]
@app.get("/tasks")
def get_list_of_task():
    # return list(map(lambda task: task.to_json(), tasks))
    # return [task.to_json() for task in tasks]

    response = []
    for task in tasks.values():
        response.append(task.to_json())
    return response


## Update task
## PUT /task/{id}
@app.put("/task/<uuid>")
def complete_task(uuid: str):
    task = tasks[uuid]
    task.complete()
    return "200"


## Delete task
## DELETE /task/{id}
@app.delete("/task/<uuid>")
def delete_task(uuid: str):
    del tasks[uuid]
    return "200"


## Menu
## GET /: str
@app.get("/")
def index():
    return render_template("index.html")


def signal_handler(sig, frame):
    print("Voce pressionou CRTL+C, encerrando...")
    escrever_tarefas_no_arquivo("./database/db.txt", tasks)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5300)
