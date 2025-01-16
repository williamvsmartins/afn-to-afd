def adicionarTransicao( automato, origem, letra, destino ):
    if origem not in automato[ "função_programa" ]:
        automato[ "função_programa" ][ origem ] = dict()
    
    if letra not in automato[ "função_programa" ][ origem ]:
        automato[ "função_programa" ][ origem ][letra] = set()
    
    automato[ "função_programa" ][ origem ][letra].add( destino )

def fecho_vazio( automato, estados ):
    fecho = set( estados )
    fila = list( estados )

    while fila:
        estado = fila.pop( 0 )
        if estado in automato[ "função_programa" ] and "" in automato[ "função_programa" ][ estado ]:
            estados_novos = automato[ "função_programa" ][ estado ][ "" ]
            for estado_novo in estados_novos:
                if estado_novo not in fecho:
                    fecho.add( estado_novo )
                    fila.append( estado_novo )
    
    return fecho

def afn_para_afd( automato ):
    afd = {
        "alfabeto" : set(),
        "estados" : set(),
        "função_programa" : dict(),
        "estado_inicial" : "0",
        "estados_finais" : set(),
    }

    afd[ "alfabeto" ].add( "$" )

    estado_inicial = ",".join( sorted( fecho_vazio( automato, { "0" } ) ) )

    afd[ "estados" ].add( estado_inicial )

    fila = [ estado_inicial ]
    visitados = set()

    while fila:
        estado_atual = fila.pop( 0 )
        if estado_atual in visitados:
            continue
        
        visitados.add( estado_atual )
        estados_atuais = estado_atual.split( "," )

        for letra in automato[ "alfabeto" ]:
            novos_estados = set()
            for estado in estados_atuais:
                if estado in automato[ "função_programa" ] \
                    and letra in automato[ "função_programa" ][ estado ]:
                    novos_estados = automato[ "função_programa" ][ estado ][ letra ]
            
            if novos_estados:
                novo_estado = ",".join( sorted( novos_estados ) )
                if novo_estado not in afd[ "estados" ]:
                    fila.append( novo_estado )
                    afd[ "estados" ].add( novo_estado )
                    estados = [ estado in automato[ "estados_finais" ] for estado in novos_estados ]
                    if any( estados ):
                        afd[ "estados_finais" ].add( novo_estado )
                adicionarTransicao( afd, estado_atual, letra, novo_estado )
            else:
                adicionarTransicao( afd, estado_atual, letra, "" )
    
    return afd
