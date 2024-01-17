from task.task import Task
from typing import Dict


def ler_tarefas_do_arquivo(caminho_do_arquivo: str) -> Dict[str, Task]:
    tarefas = {}

    try:
        with open(caminho_do_arquivo, "r") as arquivo:
            for linha in arquivo:
                uuid, prioridade, descricao, concluido = linha.strip().split(";")

                concluido = concluido.strip() == "True"
                tarefa = Task(
                    description=descricao.strip(),
                    priority=int(prioridade.strip()),
                    completed=concluido,
                    uuid=uuid,
                )
                tarefas[tarefa.uuid.hex] = tarefa
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


def escrever_tarefas_no_arquivo(caminho_do_arquivo: str, tarefas: Dict[str, Task]):
    print("dados:", len(tarefas.values()))
    try:
        with open(caminho_do_arquivo, "w") as arquivo:
            for tarefa in tarefas.values():
                prioridade = tarefa.priority
                descricao = tarefa.description
                concluido = tarefa.completed
                uuid = tarefa.uuid.hex

                arquivo.write(f"{uuid}; {prioridade}; {descricao}; {concluido}\n")
                print(f"✅ Tarefas salva: {uuid}!")
    except Exception as e:
        print(f"🚨 Erro ao escrever no arquivo: {e}")
        resposta = input("Quer tentar denovo? (s/n):").strip()
        if resposta == "s":
            escrever_tarefas_no_arquivo(caminho_do_arquivo, tarefas)
