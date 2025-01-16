# Importações necessárias
import sys
from graphviz import Digraph

# Função para adicionar transições ao autômato
def adicionarTransicao(automato, origem, letra, destino):
    if origem not in automato["função_programa"]:
        automato["função_programa"][origem] = dict()

    if letra not in automato["função_programa"][origem]:
        automato["função_programa"][origem][letra] = set()

    automato["função_programa"][origem][letra].add(destino)

# Função para calcular o fecho vazio (ε-fecho)
def fecho_vazio(automato, estados):
    fecho = set(estados)
    fila = list(estados)

    while fila:
        estado = fila.pop(0)
        if estado in automato["função_programa"] and "" in automato["função_programa"][estado]:
            estados_novos = automato["função_programa"][estado][""]
            for estado_novo in estados_novos:
                if estado_novo not in fecho:
                    fecho.add(estado_novo)
                    fila.append(estado_novo)

    return fecho

# Função para converter AFN para AFD
def afn_para_afd(automato):
    afd = {
        "alfabeto": automato["alfabeto"],
        "estados": set(),
        "função_programa": dict(),
        "estado_inicial": "0",
        "estados_finais": set(),
    }

    estado_inicial = ",".join(sorted(fecho_vazio(automato, {automato["estado_inicial"]})))
    afd["estados"].add(estado_inicial)

    fila = [estado_inicial]
    visitados = set()

    while fila:
        estado_atual = fila.pop(0)
        if estado_atual in visitados:
            continue

        visitados.add(estado_atual)
        estados_atuais = estado_atual.split(",")

        for letra in automato["alfabeto"]:
            novos_estados = set()
            for estado in estados_atuais:
                if estado in automato["função_programa"] and letra in automato["função_programa"][estado]:
                    novos_estados.update(automato["função_programa"][estado][letra])

            if novos_estados:
                novo_estado = ",".join(sorted(fecho_vazio(automato, novos_estados)))
                if novo_estado not in afd["estados"]:
                    fila.append(novo_estado)
                    afd["estados"].add(novo_estado)
                    if any(est in automato["estados_finais"] for est in novos_estados):
                        afd["estados_finais"].add(novo_estado)

                adicionarTransicao(afd, estado_atual, letra, novo_estado)

    return afd

# Função para imprimir a função programa
def printFuncaoPrograma(automato):
    for origem, transicoes in automato["função_programa"].items():
        for letra, destinos in transicoes.items():
            for destino in destinos:
                print(f"{origem} -- {letra} --> {destino}")

# Função para gerar gráficos dos autômatos usando Graphviz
def gerar_grafico(automato, nome="automato"):
    dot = Digraph(comment="Automato", format="png")

    # Adiciona os estados
    for estado in automato["estados"]:
        if estado in automato["estados_finais"]:
            dot.node(estado, shape="doublecircle")
        else:
            dot.node(estado)

    # Adiciona as transições
    for origem, transicoes in automato["função_programa"].items():
        for letra, destinos in transicoes.items():
            for destino in destinos:
                label = letra if letra else "ε"
                dot.edge(origem, destino, label=label)

    # Adiciona o estado inicial
    dot.node("start", shape="point")
    dot.edge("start", automato["estado_inicial"])

    # Renderiza o gráfico
    dot.render(nome, cleanup=True)
    print(f"Gráfico gerado: {nome}.png")