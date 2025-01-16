import sys
from automata import *

def base():
    afn = {
        "alfabeto" : { "a", "b" },
        "estados" : { "0", "1", "2", "3" },
        "função_programa" : dict(),
        "estado_inicial" : "0",
        "estados_finais" : { "0", "3" },
    }

    adicionarTransicao( afn, "0", "a", "2" )
    adicionarTransicao( afn, "0", "a", "3" )
    adicionarTransicao( afn, "2", "b", "1" )
    adicionarTransicao( afn, "1", "b", "0" )

    print( "Autômato Finito Não Determinístico:\n" )
    print( "\nTransições do AFN:\n" )
    printFuncaoPrograma( afn )

    print()

    afd = afn_para_afd( afn )

    print( "Autômato Finito Determinístico:\n" )
    printAutomato( afd )
    print( "\nTransições do AFD:\n" )
    printFuncaoPrograma( afd )


def main():

    afn = {
        "alfabeto" : set(),
        "estados" : set(),
        "função_programa" : dict(),
        "estado_inicial" : "0",
        "estados_finais" : set(),
    }

    estados = input( "Informe os estados do autômato:\n" ).split( ", " )
    for estado in afn[ "estados" ]:
        afn[ "estados" ][ estado ] = afn[ "estados" ][ estado ].strip()
    estado_inicial = input( "Informe o estado inicial:\n" ).strip()
    print( "Informe a função programa:" )
    transicoes = list()
    alfabeto = set()
    qtd_transicoes = 0
    while qtd_transicoes <= 8:
        transicao = input()

        if ( transicao == "Encerrar transições" ):
            break

        if len( transicao ) != 3:
            raise Exception( "Transição inválida!" )
        transicoes.append( [ transicao[ 0 ], transicao[ 1 ], transicao[ 2 ] ] )
        if ( transicao[ 1 ] not in alfabeto ):
            alfabeto.add( transicao[ 1 ] )
        qtd_transicoes += 1

    estados_finais = input( "Informe os estados finais:\n" ).split( ", " )
    print( estados )
    print( estado_inicial )
    print( alfabeto )
    print( transicoes )
    print( estados_finais )

    afn[ "alfabeto" ] = alfabeto
    afn[ "estados" ] = set( estados )
    afn[ "estado_inicial" ] = estado_inicial
    afn[ "estados_finais" ] = set( estados_finais )

    for transicao in transicoes:
        adicionarTransicao( afn, transicao[ 0 ], transicao[ 1 ], transicao[ 2 ] )

    print( "Autômato Finito Não Determinístico:\n" )
    printAutomato( afn )
    print( "\nTransições do AFN:\n" )
    printFuncaoPrograma( afn )

    afd = afn_para_afd( afn )

    print( "Autômato Finito Determinístico:\n" )
    printAutomato( afd )
    print( "\nTransições do AFD:\n" )
    printFuncaoPrograma( afd )

if __name__ == "__main__":
    if len( sys.argv ) > 1 and sys.argv[1] == "--base":
        base()
    else:
        main()