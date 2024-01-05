from task.display import exibir_tarefas
from task.task import Task
from typing import List


def adicionar_tarefa(tarefas: List[Task]):
    descricao = input("Descrição da tarefa: ")
    prioridade = input("Qual a prioridade da tarefa? (1,2,3): ")

    # validar a prioridade

    tarefa = Task(description=descricao, priority=prioridade)
    tarefas.append(tarefa)

    print("\n>>>Tarefa Adicionada<<<")


def remover_tarefa(tarefas):
    if len(tarefas) == 0:
        print("\n>>>Nenhuma Tarefa<<<")

    exibir_tarefas(tarefas)
    indice = int(input("Número da terefa para remover: ")) - 1

    if 0 <= indice < len(tarefas):
        # del tarefas[indice]

        tarefas[indice] = tarefas[len(tarefas) - 1]
        tarefas.pop()

        print("\n>>>Tarefa Removida<<<")
    else:
        print("\n>>>Número de tarefa inválido<<<")


def concluir_tarefa(tarefas: List[Task]):
    if len(tarefas) == 0:
        print("\n>>>Nenhuma Tarefa<<<")

    exibir_tarefas(tarefas)
    indice = int(input("Número da tarefa que deseja concluir: ")) - 1

    if 0 <= indice < len(tarefas):
        tarefas[indice].complete()
        
        print("\n>>>✅ Tarefa concluida<<<")
    else:
        print("\nTarefa inválida")
