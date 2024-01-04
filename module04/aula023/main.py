from task.operations import adicionar_tarefa, remover_tarefa, concluir_tarefa
from module04.aula024.database.db import ler_tarefas_do_arquivo, escrever_tarefas_no_arquivo
from task.display import exibir_tarefas


# Task manager


def menu():
    caminho_do_arquivo = "./database/db.txt"
    tarefas = ler_tarefas_do_arquivo(caminho_do_arquivo)

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
            escrever_tarefas_no_arquivo(caminho_do_arquivo, tarefas)
            break
        else:
            print("\nOpção inválida")


menu()
