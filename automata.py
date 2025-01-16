def adicionarTransicao( automato, origem, letra, destino ):
    if origem not in automato[ "função_programa" ]:
        automato[ "função_programa" ][ origem ] = dict()
    
    if letra not in automato[ "função_programa" ][ origem ]:
        automato[ "função_programa" ][ origem ][letra] = set()
    
    automato[ "função_programa" ][ origem ][letra].add( destino )
