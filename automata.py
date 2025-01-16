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