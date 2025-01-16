import sys
from graphviz import Digraph

# Função para adicionar transições ao autômato
# Recebe o autômato, o estado de origem, a letra da transição e o estado de destino
def adicionar_transicao(automato, origem, letra, destino):
    # Inicializa o dicionário para o estado de origem, se ainda não existir
    if origem not in automato["função_programa"]:
        automato["função_programa"][origem] = {}

    # Inicializa o conjunto de destinos para a letra, se ainda não existir
    if letra not in automato["função_programa"][origem]:
        automato["função_programa"][origem][letra] = set()

    # Adiciona o estado de destino à transição
    automato["função_programa"][origem][letra].add(destino)

# Função para calcular o fecho vazio (ε-fecho) de um conjunto de estados
# Permite alcançar estados via transições vazias (ε-transições)
def fecho_vazio(automato, estados):
    fecho = set(estados)  # Inicializa o fecho com os estados fornecidos
    fila = list(estados)  # Fila para processamento iterativo

    while fila:
        estado = fila.pop(0)  # Remove o próximo estado da fila
        # Verifica se o estado tem transições vazias (ε)
        if estado in automato["função_programa"] and "" in automato["função_programa"][estado]:
            estados_novos = automato["função_programa"][estado][""]
            for estado_novo in estados_novos:
                # Adiciona novos estados ao fecho, se ainda não estiverem presentes
                if estado_novo not in fecho:
                    fecho.add(estado_novo)
                    fila.append(estado_novo)

    return fecho

# Função para converter um Autômato Finito Não-determinístico (AFN) para Determinístico (AFD)
def afn_para_afd(automato):
    # Inicializa a estrutura do AFD
    afd = {
        "alfabeto": automato["alfabeto"],
        "estados": set(),
        "função_programa": {},
        "estado_inicial": None,
        "estados_finais": set(),
    }

    # Calcula o estado inicial do AFD a partir do fecho vazio do estado inicial do AFN
    estado_inicial = ",".join(sorted(fecho_vazio(automato, {automato["estado_inicial"]})))
    afd["estado_inicial"] = estado_inicial
    afd["estados"].add(estado_inicial)

    fila = [estado_inicial]  # Fila para processar estados do AFD
    visitados = set()  # Conjunto de estados já processados

    while fila:
        estado_atual = fila.pop(0)  # Remove o próximo estado da fila
        if estado_atual in visitados:
            continue

        visitados.add(estado_atual)  # Marca o estado como visitado
        estados_atuais = estado_atual.split(",")  # Divide o estado em múltiplos estados do AFN

        for letra in automato["alfabeto"]:
            novos_estados = set()
            for estado in estados_atuais:
                # Verifica transições para a letra atual
                if estado in automato["função_programa"] and letra in automato["função_programa"][estado]:
                    novos_estados.update(automato["função_programa"][estado][letra])

            if novos_estados:
                # Calcula o novo estado do AFD a partir do fecho vazio dos novos estados
                novo_estado = ",".join(sorted(fecho_vazio(automato, novos_estados)))
                if novo_estado not in afd["estados"]:
                    fila.append(novo_estado)  # Adiciona o novo estado para processamento futuro
                    afd["estados"].add(novo_estado)
                    # Verifica se o novo estado é um estado final
                    if any(est in automato["estados_finais"] for est in novos_estados):
                        afd["estados_finais"].add(novo_estado)

                # Adiciona a transição ao AFD
                adicionar_transicao(afd, estado_atual, letra, novo_estado)

    return afd

# Função para imprimir a função programa do autômato
# Exibe todas as transições no formato: origem -- letra --> destino
def print_funcao_programa(automato):
    for origem, transicoes in automato["função_programa"].items():
        for letra, destinos in transicoes.items():
            for destino in destinos:
                print(f"{origem} -- {letra} --> {destino}")

# Função para gerar um gráfico visual do autômato utilizando Graphviz
def gerar_grafico(automato, nome="automato"):
    dot = Digraph(comment="Automato", format="png")

    # Adiciona os estados ao gráfico
    for estado in automato["estados"]:
        if estado in automato["estados_finais"]:
            dot.node(estado, shape="doublecircle")  # Estado final
        else:
            dot.node(estado)  # Estado comum

    # Adiciona as transições ao gráfico
    for origem, transicoes in automato["função_programa"].items():
        for letra, destinos in transicoes.items():
            for destino in destinos:
                label = letra if letra else "ε"  # Mostra ε para transições vazias
                dot.edge(origem, destino, label=label)

    # Renderiza e salva o gráfico
    dot.render(nome, cleanup=True)
    print(f"Gráfico gerado: {nome}.png")
