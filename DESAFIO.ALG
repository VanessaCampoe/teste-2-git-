Algoritmo "Desafio"
//Escreva um programa para calcular a redu��o do tempo de vida de um fumante.
//Pergunte a quantidade de cigarros fumados por dias e quantos anos ele j� fumou.
//Considere que um fumante perde 10 min de vida a cada cigarro.
//Calcule quantos dias de vida um fumante perder� e exiba o total em dias.
Var
   cigarros_por_dia: inteiro
   anos_fumando : inteiro
   total_cigarros : inteiro
   dias_perdidos : real

Inicio

    escreva("Quantos cigarros voc� fuma por dia? ")
    leia(cigarros_por_dia)

    escreva("H� quantos anos voc� fuma? ")
    leia(anos_fumando)
    
    total_cigarros <- cigarros_por_dia * 365 * anos_fumando

    dias_perdidos <- (total_cigarros * 10) / 1440

    escreva("Voc� perder� aproximadamente ", dias_perdidos, " dias de vida.")
    
    
    
Fimalgoritmo