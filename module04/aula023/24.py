from typing import Dict, List


def ler_tarefas_do_arquivo(caminho_do_arquivo: str) -> List[Dict[str, bool]]:
    tarefas = []
    try:
        with open(caminho_do_arquivo, "r") as arquivo:
            for linha in arquivo:
                descricao, concluido = linha.strip().split(";")
                tarefa = {
                    "descricao": descricao,
                    "concluido": concluido.strip() == "True",
                }
                tarefas.append(tarefa)
    except FileNotFoundError:
        print(f"🚨 Arquivo não encontrado: {caminho_do_arquivo}")
        resposta = input("Deseja digitar outro caminho? (s/n):").strip()
        if resposta == "s":
            caminho_do_arquivo = input("Qual?:").strip()
            ler_tarefas_do_arquivo(caminho_do_arquivo)

    except Exception as e:
        print(f"🚨 Erro ao ler o arquivo: {e}")
        resposta = input("Quer tentar denovo? (s/n):").strip()
        if resposta == "s":
            ler_tarefas_do_arquivo(caminho_do_arquivo)
    else:
        print("✅ Tarefas carregadas com sucesso.")
    finally:
        return tarefas


def escrever_tarefas_no_arquivo(
    caminho_do_arquivo: str,
    tarefas: List[Dict[str, bool]]
):
    try:
        with open(caminho_do_arquivo, "w") as arquivo:
            for tarefa in tarefas:
                descricao = tarefa["descricao"]
                concluido = tarefa["concluido"]
                arquivo.write(f"{descricao}; {concluido}\n")
    except Exception as e:
        print(f"🚨 Erro ao escrever no arquivo: {e}")
        resposta = input("Quer tentar denovo? (s/n):").strip()
        if resposta == "s":
            escrever_tarefas_no_arquivo(caminho_do_arquivo, tarefas)
    else:
        print("✅ Tarefas salvas com sucesso.")
