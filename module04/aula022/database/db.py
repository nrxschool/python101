from typing import Dict, List


def ler_tarefas_do_arquivo(caminho_do_arquivo: str) -> List[Dict[str, bool]]:
    tarefas = []

    with open(caminho_do_arquivo, "r") as arquivo:
        for linha in arquivo:
            descricao, concluido = linha.strip().split(";")
            tarefa = {"descricao": descricao, "concluido": concluido.strip() == "True"}
            tarefas.append(tarefa)

    return tarefas

