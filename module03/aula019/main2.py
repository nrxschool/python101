import copy

original = {"a": 1, "b": [2, 3]}


novo = copy.deepcopy(original)

novo["cidade"] = "sao paulo"
novo["b"][0] = 999

print(original)


def exibir_tarefas(tarefas):
    print(f"\nVc tem {len(tarefas)} Tarefas")

    # quantas tarefas feitas?
    # quantas tarefas nao feitas?

    if len(tarefas) == 0:
        print("\n>>>Nunhuma tarefa!<<<")

    for indice, tarefa in enumerate(tarefas):
        descricao = tarefa["descricao"]
        concluida = tarefa["concluida"]
        status = "Concluída" if concluida else "Não Concluída"

        print(f"{indice + 1}. {descricao} - {status}")


def adicionar_tarefa(tarefas):
    descricao = input("Descrição da tarefa: ")

    tarefa = {"descricao": descricao, "concluida": False}
    tarefas.append(tarefa)

    print("\n>>>Tarefa adicionada.<<<")


def remover_tarefa(tarefas):
    if len(tarefas) == 0:
        print("\n>>>Nunhuma tarefa!<<<")
        return

    exibir_tarefas(tarefas)
    indice = int(input("Número da tarefa para remover: ")) - 1

    if 0 <= indice < len(tarefas):
        tarefas[indice] = tarefas[len(tarefas) - 1]
        tarefas.pop()
        # del tarefas[indice]

        print("\n>>>Tarefa removida.<<<")
    else:
        print("\nNúmero de tarefa inválido.")


def concluir_tarefa(tarefas):
    if len(tarefas) == 0:
        print("\n>>>Nunhuma tarefa!<<<")
        return

    exibir_tarefas(tarefas)
    indice = int(input("Número da tarefa para concluir: ")) - 1

    if 0 <= indice < len(tarefas):
        tarefa = tarefas[indice]
        tarefa["concluido"] = True
        tarefas[indice] = tarefa

        print("\n>>>Tarefa concluída.<<<")
    else:
        print("\nNúmero de tarefa inválido.")


def menu():
    tarefas = []
    while True:
        print("\nGerenciador de Tarefas")
        print("1. Ver Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Remover Tarefa")
        print("4. Concluir Tarefa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            remover_tarefa(tarefas)
        elif opcao == "4":
            concluir_tarefa(tarefas)
        elif opcao == "5":
            print("\n>>>Saindo do programa.<<<\n")
            break
        else:
            print("\nOpção inválida.")


menu()
