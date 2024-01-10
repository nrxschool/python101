from datetime import datetime
import uuid as uuid_class


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
