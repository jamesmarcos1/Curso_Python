vida = 10
dano = 2

vida_inimigo = 6

loop = True

def main():
    global vida_inimigo
    global vida
    print("Você encontrou um inimigo:")
    print("vida: " + str(vida) )
    print("1: Atacar")
    print("2: Furgir")
    
    escolha = int(input("Digite sua escolha:"))
    
    if escolha == 1:
        while vida_inimigo > 0:
            vida_inimigo -= 2
            vida -= 1
            print("Você Atacou")
            print("vida inimigo " + str(vida_inimigo))
            print("Sua vida " + str(vida))
            if vida_inimigo == 0:
                print("Inimigo morto")
    elif escolha == 2:
        print("Você esta com medo? ")
        return True
    else:
        print("Seu comando não faz sentido -_-")
        return False
    
while loop:
    loop = not main()