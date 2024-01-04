from task.display import exibir_tarefas


def adicionar_tarefa(tarefas):
    descricao = input("Descrição da tarefa: ")

    tarefa = {"descricao": descricao, "concluido": False}
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


def concluir_tarefa(tarefas):
    if len(tarefas) == 0:
        print("\n>>>Nenhuma Tarefa<<<")

    exibir_tarefas(tarefas)
    indice = int(input("Número da tarefa que deseja concluir: ")) - 1

    if 0 <= indice < len(tarefas):
        tarefa = tarefas[indice]
        tarefa["concluido"] = True
        tarefas[indice] = tarefa

        print("\n>>>✅ Tarefa concluida<<<")
    else:
        print("\nTarefa inválida")
