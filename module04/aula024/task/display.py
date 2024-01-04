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
