# Task manager


def adicionar_tarefa(tarefas):
    descricao = input("Descrição da tarefa: ")

    tarefa = {"descricao": descricao, "concluido": False}
    tarefas.append(tarefa)

    print("\n>>>Tarefa Adicionada<<<")


def exibir_tarefas(tarefas):
    print(f"\nVc tem {len(tarefas)} Tarefas")

    # Quantas tarefas feitas?
    # Quantas tarefas nao feitas?

    if len(tarefas) == 0:
        print("\n>>>Nenhuma Tarefa<<<")

    for indice, tarefa in enumerate(tarefas):
        descricao = tarefa["descricao"]
        concluido = tarefa["concluido"]

        status = "Concluída" if concluido else "Não Concluída"

        print(f"{indice + 1}. {descricao} - {status}")


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


def menu():
    tarefas = []

    while True:
        print("\n📚 Gerenciador de tarefas")
        print("1. Ver todas as tarefas")
        print("2. Adicionar uma tarefa")
        print("3. Remover uma tarefa")
        print("4. Concluir uma tarefa")
        print("5. Sair")

        opcao = input("Escolha sua opção: ")

        if opcao == "1":
            exibir_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            remover_tarefa(tarefas)
        elif opcao == "4":
            concluir_tarefa(tarefas)
        elif opcao == "5":
            print("\n>>>Saindo do programa<<<\n")
            break
        else:
            print("\nOpção inválida")


menu()
