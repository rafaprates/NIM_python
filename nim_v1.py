def msg(comp, n, retira):
    print()
    if comp == True:
        print("O computador tirou", retira ,"peça(s)")
    else:
        print("Você tirou", retira, "peça(s).")
    print("Agora resta(m)", n, "peça(s)")
    print()

def campeonato():
    rodada = 1
    while rodada <= 3:
        print()
        print("**** Rodada", rodada, "****")
        print()
        rodada = rodada + 1
        partida()
    print()
    print("**** Final do campeonato! ****")
    print()
    #print("Placar: Você", usrScore, "X", compScore, "Computador")

def computador_escolhe_jogada(n, m):
    if m == minPieces: 
        compRetira = minPieces
    else:
        compRetira = m
        pecasRestantes = n - compRetira
        while pecasRestantes  % (m+1) != 0:
            compRetira = compRetira - 1
            pecasRestantes = n - compRetira
    return compRetira #o n. de peças que o comp retira.

def usuario_escolhe_jogada(n, m):
    usrRetira = int(input("Quantas peças você vai tirar? "))
    while usrRetira > m or usrRetira < 1: #verifica se jogada é válida.
        print()
        print("Oops! Jogada inválida! Tente de novo.")
        print()
        usrRetira = int(input("Quantas peças você vai tirar? "))
    return usrRetira #o n. de peças que o usuário retira.

def partida():
    n = int(input("Quantas peças? "))
    while n <= 0: #verifica se o n. de peças é valido.
        print("O número de peças deve ser maior que um.")
        n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    while m <= 0 or m >= n: #verifica se o limite é válido.
        print("O limite de peças deve ser maior que um.")
        m = int(input("Limite de pelas por jogada?"))
    print()
    rodada = 1
    if rodada == 1: #inicia o placar.
        compScore = 0
        usrScore = 0
#***** PRIMEIRA JOGADA INICIA AQUI *****
    if n % (m+1) == 0:
        comp = False #informa quem começou. E passa parâmetro para msg().
        print("Você começa!")
        usrRetira = usuario_escolhe_jogada(n, m)
        n = n - usrRetira #n. de peças restantes
    else:
        comp = True #informa quem começou. E passa parâmetro para msg().
        print("Computador começa!")
        compRetira = computador_escolhe_jogada(n, m)
        n = n - compRetira #n. de peças restantes
        msg(comp, n, compRetira)
#***** A PRIMEIRA JOGADA TERMINA AQUI *****
    while n > 0: #main loop
        if comp == True: #se comp começou, usuário joga a prox.
            comp = False #indica à msg() que tipo deve ser imprimido.
            usrRetira = usuario_escolhe_jogada(n, m)
            n = n - usrRetira
            msg(comp, n, compRetira)
        else:
            comp = True #indica à msg() que tipo deve ser imprimido.
            compRetira = computador_escolhe_jogada(n, m)
            n = n - compRetira
            msg(comp, n, compRetira)
    if comp == True: #se na última rodada comp = True. Comp jogou por último e venceu.
        compScore = compScore + 1
    else:
        usrScore = usrScore + 1
    if compScore > usrScore:
        print("Fim do jogo! O computador ganhou!")
    else:
        print("Fim do jogo! Você ganhou") #nunca será chamada
    print()


def main():
    print()
    print("Bem-vindo ao jogo NIM! Escolha:")
    print()
    print("1 - para jogar uma partida isolada")
    usrOption = int(input("2 - para jogar um campeonato "))
    print()
    if usrOption == 1:
        print("Você escolheu uma partida!")
        partida()
    elif usrOption == 2:
        print("Você escolheu um campeonato!")
        campeonato()
    else:
        print("Opção inválida!")

minPieces = 1
main()
