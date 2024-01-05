from task.task import Task
from typing import List


def ler_tarefas_do_arquivo(caminho_do_arquivo: str) -> List[Task]:
    tarefas = []

    try:
        with open(caminho_do_arquivo, "r") as arquivo:
            for linha in arquivo:
                prioridade, descricao, concluido = linha.strip().split(";")

                concluido = concluido.strip() == "True"
                tarefa = Task(
                    description=descricao.strip(),
                    priority=int(prioridade.strip()),
                    completed=concluido,
                )
                tarefas.append(tarefa)
    except FileNotFoundError:
        print(f"🚨 Arquivo não encontrado: {caminho_do_arquivo}")
        resposta = input("Quer digital outro caminho? (s/n):").strip()
        if resposta == "s":
            caminho_do_arquivo = input("Qual?:").strip()
            return ler_tarefas_do_arquivo(caminho_do_arquivo)
        raise FileNotFoundError()

    except Exception as e:
        print(f"🚨 Erro ao ler o arquivo: {e}")
        resposta = input("Quer tentar denovo? (s/n):").strip()
        if resposta == "s":
            return ler_tarefas_do_arquivo(caminho_do_arquivo)
    else:
        print(">>>✅ Tarefas carregadas com sucesso.<<<")
        return tarefas


def escrever_tarefas_no_arquivo(caminho_do_arquivo: str, tarefas: List[Task]):
    try:
        with open(caminho_do_arquivo, "w") as arquivo:
            for tarefa in tarefas:
                prioridade = tarefa.priority
                descricao = tarefa.description
                concluido = tarefa.completed

                arquivo.write(f"{prioridade}; {descricao}; {concluido}\n")
    except Exception as e:
        print(f"🚨 Erro ao escrever no arquivo: {e}")
        resposta = input("Quer tentar denovo? (s/n):").strip()
        if resposta == "s":
            escrever_tarefas_no_arquivo(caminho_do_arquivo, tarefas)
    else:
        print(">>>✅ Tarefas salvas com sucesso.<<<")
