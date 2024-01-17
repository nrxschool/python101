from datetime import datetime
from urllib import request
import uuid as uuid_class
from typing import List
import json



class Task:
    def __init__(
        self, description: str, priority: int, completed: bool = False, uuid: str = None
    ) -> None:
        self.description = description
        self.priority = priority
        self.completed = completed
        self.start_time = datetime.now()
        self.time_spent = None
        self.uuid = uuid_class.uuid4() if not uuid else uuid_class.UUID(hex=uuid)

    def complete(self):
        self.completed = True
        self.time_spent = datetime.now() - self.start_time

    def __str__(self) -> str:
        completed_status = "✅" if self.completed else "⏰"
        if self.time_spent == None:
            time = "Nenhum"
        else:
            hours, remainder = divmod(self.time_spent.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            time = f"{hours:02}:{minutes:02}:{seconds:02}"
        return f"[{self.priority}] - descrição: {self.description} (concluido: {completed_status}, tempo gasto: {time})"

    def __repr__(self) -> str:
        start_time_fmt = self.start_time.strftime("%Y-%m-%d %H:%M:%S")
        time_spent_fmt = self.time_spent if self.time_spent is not None else "None"
        return (
            f"Task(uuid='{self.uuid}', description='{self.description}', priority={self.priority}, "
            f"completed={self.completed}, start_time='{start_time_fmt}', "
            f"time_spent={time_spent_fmt})"
        )

    def to_json(self):
        return {
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
            "time_spent": str(self.time_spent) if self.time_spent else None,
            "uuid": self.uuid.hex,
        }


class TaskClient:
    def __init__(self, base_url: str = "http://127.0.0.1:5000") -> None:
        self.base_url: str = base_url

    def get_all_tasks(self) -> List[Task]:
        # criar a rota
        route = self.base_url + "/tasks"
        # conectar no server na rota '/tasks'
        req = request.Request(route, method="GET")
        # deserializar os dados
        with request.urlopen(req) as f:
            response = f.read().decode("utf-8")
        # retorno o resultado

        return json.loads(response)

    def get_task(self, uuid: str) -> Task:
        # criar a rota
        route = self.base_url + "/task/" + uuid
        # conectar no server na rota '/tasks'
        req = request.Request(route, method="GET")
        # deserializar os dados
        with request.urlopen(req) as f:
            response = f.read().decode("utf-8")

        # retorno o resultado
        return json.loads(response)

    def add_task(self, description: str, priority: int) -> str:
        # montar o dado
        data = {"description": description, "priority": priority, "completed": False}
        # serializar os dados
        data = json.dumps(data).encode("utf-8")
        # criar a rota
        route = self.base_url + "/task"
        # conectar no server na rota '/tasks'
        req = request.Request(route, method="POST", data=data)
        req.add_header("Content-Type", "application/json")
        # deserializar os dados
        with request.urlopen(req) as f:
            response = f.read().decode("utf-8")
        # retorno o resultado

        return json.loads(response)

    def update_task(self, uuid: str) -> Task:
        # criar a rota
        route = self.base_url + "/task/" + uuid
        # conectar no server na rota '/tasks'
        req = request.Request(route, method="PUT")
        # deserializar os dados
        with request.urlopen(req) as f:
            response = f.read().decode("utf-8")

        # retorno o resultado
        return json.loads(response)

    def delete_task(self, uuid: str) -> Task:
        # criar a rota
        route = self.base_url + "/task/" + uuid
        # conectar no server na rota '/tasks'
        req = request.Request(route, method="DELETE")
        # deserializar os dados
        with request.urlopen(req) as f:
            response = f.read().decode("utf-8")

        # retorno o resultado
        return json.loads(response)

BASE_URL = "http://137.184.228.104:3000"

client = TaskClient(base_url=BASE_URL)

print(client.update_task(uuid="0591c2a85c6e433fb639e98d39ef62ca"))
