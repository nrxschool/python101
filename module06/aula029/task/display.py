from typing import List
from task.task import Task


def exibir_tarefas(tarefas: List[Task]):
    # organizar a lista de tarefas pela prioridade

    print(f"\nVc tem {len(tarefas)} Tarefas")

    if len(tarefas) == 0:
        print("\n>>>Nenhuma Tarefa<<<")

    for indice, tarefa in enumerate(tarefas):
        print(f"{indice + 1}. {str(tarefa)}")
