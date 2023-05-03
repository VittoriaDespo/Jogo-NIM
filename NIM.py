def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    computador_comeca = True
    print(" ")
    if n % (m+1)==0:
        computador_comeca = False
        print("Você começa!")      
    else:
        print("Computador começa!")    
    while n > 0:
        if computador_comeca:
            jogada = computador_escolhe_jogada(n,m)
            if jogada == 1:
                print("\nO computador tirou uma peça.")
            else:
                print("\nO computador tirou",jogada,"peças.")
            computador_comeca = False
        else:
            jogada = usuario_escolhe_jogada(n,m)
            if jogada == 1:
                print("\nVocê tirou uma peça.")
            else:
                print("\nVocê tirou",jogada,"peças.") 
            computador_comeca = True
        n = n-jogada
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")
        elif n == 0 and computador_comeca == False:
            print("O computador ganhou!")
            return 0
        elif n == 0 and computador_comeca == True:
            print("Você ganhou!")
            return 1
        else:
            print("Agora restam",n,"peças no tabuleiro.\n")
            
        
def computador_escolhe_jogada(n,m): 
    if n <= m:
        return n
    elif n % (m + 1) > 0:
        return n % (m +1)
    return m
    
def usuario_escolhe_jogada(n,m):
    jog_usuario = int(input("Quantas peças você vai tirar? "))
    while jog_usuario > m or jog_usuario > n or jog_usuario < 1:
        print("Oops! Jogada inválida! Tente de novo.")
        jog_usuario = int(input("Quantas peças você vai tirar? "))
    return jog_usuario
    
def campeonato():
    rodada = 0
    usuario = 0
    computador = 0
    while rodada <= 2:
        rodada = rodada + 1
        print("*** Rodada",rodada,"***")
        if partida() == 1:
            usuario = usuario + 1
        else:
            computador = computador + 1
    print("\n**** Final do campeonato! ****")
    print("Placar: Você",usuario,"X",computador,"Computador")
    

print("Bem-vindo ao jogo do NIM!")
print("Escolha:")
sel = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
while sel < 1 or sel > 2:
    print("Opção invalida")
    sel = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
if sel==1:
    print("\nVoce escolheu uma partida isolada!\n")
    print("***Inicio***")
    partida() 
elif sel==2:
    print("\nVoce escolheu um campeonato!")
    campeonato()    





    

