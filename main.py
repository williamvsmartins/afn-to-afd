import sys
from automata import *

# Função para executar a configuração base do autômato
# Inclui um exemplo pré-definido de AFN e sua conversão para AFD
def base():
    afn = {
        "alfabeto": {"a", "b"},  # Alfabeto do autômato
        "estados": {"0", "1", "2", "3"},  # Conjunto de estados
        "função_programa": {},  # Transições do autômato
        "estado_inicial": "0",  # Estado inicial
        "estados_finais": {"3"},  # Conjunto de estados finais
    }

    # Definição das transições do autômato
    adicionar_transicao(afn, "0", "a", "2")
    adicionar_transicao(afn, "0", "a", "3")
    adicionar_transicao(afn, "2", "b", "1")
    adicionar_transicao(afn, "1", "b", "0")

    # Exibe e gera o gráfico do AFN
    print("Autômato Finito Não Determinístico:")
    print_funcao_programa(afn)
    gerar_grafico(afn, nome="afn")

    # Converte o AFN para AFD
    afd = afn_para_afd(afn)

    # Exibe e gera o gráfico do AFD
    print("\nAutômato Finito Determinístico:")
    print_funcao_programa(afd)
    gerar_grafico(afd, nome="afd")

# Função principal para criar um autômato interativo
def main():
    afn = {
        "alfabeto": set(),  # Inicializa o alfabeto vazio
        "estados": set(),  # Inicializa o conjunto de estados vazio
        "função_programa": {},  # Inicializa as transições vazias
        "estado_inicial": "0",  # Define um estado inicial padrão
        "estados_finais": set(),  # Inicializa o conjunto de estados finais vazio
    }

    # Solicita os estados do autômato
    estados = input("Informe os estados do autômato (separados por vírgulas):\n").split(",")
    afn["estados"] = {estado.strip() for estado in estados}

    # Solicita o estado inicial
    estado_inicial = input("Informe o estado inicial:\n").strip()
    afn["estado_inicial"] = estado_inicial

    # Solicita os estados finais
    estados_finais = input("Informe os estados finais (separados por vírgulas):\n").split(",")
    afn["estados_finais"] = {estado.strip() for estado in estados_finais}

    # Solicita as transições do autômato
    print("Informe as transições no formato origem,letra,destino (ou 'fim' para encerrar):")
    while True:
        transicao = input()
        if transicao.lower() == "fim":  # Condição de saída
            break
        # Divide a transição no formato esperado
        origem, letra, destino = transicao.split(",")
        adicionar_transicao(afn, origem.strip(), letra.strip(), destino.strip())  # Adiciona a transição
        afn["alfabeto"].add(letra.strip())  # Adiciona a letra ao alfabeto

    # Exibe e gera o gráfico do AFN
    print("\nAutômato Finito Não Determinístico:")
    print_funcao_programa(afn)
    gerar_grafico(afn, nome="afn_interativo")

    # Converte o AFN para AFD
    afd = afn_para_afd(afn)

    # Exibe e gera o gráfico do AFD
    print("\nAutômato Finito Determinístico:")
    print_funcao_programa(afd)
    gerar_grafico(afd, nome="afd_interativo")

# Executa a função base ou a principal dependendo dos argumentos fornecidos
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--base":
        base()  # Executa a configuração base
    else:
        main()  # Executa a configuração interativa
