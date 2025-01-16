import sys
from automata import *
def base():
    afn = {
        "alfabeto": {"a", "b"},
        "estados": {"0", "1", "2", "3"},
        "função_programa": dict(),
        "estado_inicial": "0",
        "estados_finais": {"3"},
    }

    adicionarTransicao(afn, "0", "a", "2")
    adicionarTransicao(afn, "0", "a", "3")
    adicionarTransicao(afn, "2", "b", "1")
    adicionarTransicao(afn, "1", "b", "0")

    print("Autômato Finito Não Determinístico:")
    printFuncaoPrograma(afn)
    gerar_grafico(afn, nome="afn")

    afd = afn_para_afd(afn)

    print("\nAutômato Finito Determinístico:")
    printFuncaoPrograma(afd)
    gerar_grafico(afd, nome="afd")

# Função principal para interatividade
def main():
    afn = {
        "alfabeto": set(),
        "estados": set(),
        "função_programa": dict(),
        "estado_inicial": "0",
        "estados_finais": set(),
    }

    estados = input("Informe os estados do autômato (separados por vírgulas):\n").split(",")
    afn["estados"] = set(estado.strip() for estado in estados)

    estado_inicial = input("Informe o estado inicial:\n").strip()
    afn["estado_inicial"] = estado_inicial

    estados_finais = input("Informe os estados finais (separados por vírgulas):\n").split(",")
    afn["estados_finais"] = set(estado.strip() for estado in estados_finais)

    print("Informe as transições no formato origem,letra,destino (ou 'fim' para encerrar):")
    while True:
        transicao = input()
        if transicao.lower() == "fim":
            break
        origem, letra, destino = transicao.split(",")
        adicionarTransicao(afn, origem.strip(), letra.strip(), destino.strip())
        afn["alfabeto"].add(letra.strip())

    print("\nAutômato Finito Não Determinístico:")
    printFuncaoPrograma(afn)
    gerar_grafico(afn, nome="afn_interativo")

    afd = afn_para_afd(afn)

    print("\nAutômato Finito Determinístico:")
    printFuncaoPrograma(afd)
    gerar_grafico(afd, nome="afd_interativo")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--base":
        base()
    else:
        main()