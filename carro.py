import funcoes
menu = ""
# Consumo
consumo = float(input("Quantos KM seu carro roda com 1L?\n"))
carro = funcoes.Carro(consumo)
#menu
while (menu!= "sair"):
    menu = input("\tMENU\n -GASOLINA\n -ANDAR\n -SAIR\n")
    menu = menu.lower()
    if menu == "gasolina":
      #Você quer Gasolina??
      op = 0
      while(op!=1 and op!=2):
        # Adicionar Gasolina
        op = input("Você quer adicionar Gasolina?\n ")
        op = funcoes.simOuNao(op)

        #Logica
        if op == 1:
            combustivel = float(input("Quantos Litros?\n "))
            carro.adicionarGasolina(combustivel)
        elif op == 2:
            print("")
        else:
            print("Digite sim ou não\n")

      #Quer ver o tanque??
      op=0
      while(op!=1 and op!=2):
        # sim ou nao?
        op = input("Você quer ver seu nível de combustível?\n ")
        op = funcoes.simOuNao(op)

        #Logica
        if op == 1:
           carro.obterGasolina()
        elif op == 2:
           print("")
        else:
          print("Digite sim ou não\n")
    elif menu == "andar":
        # VRUUUUMMM
        op=0
        while(op!=1 and op!=2):
            #Sim ou nao?
            op = input("Você quer dá uma volta?\n ")
            op = funcoes.simOuNao(op)

            #Logica
            if op == 1:
                distancia = float(input("Quantos KM de distância? \n"))
                carro.andar(distancia)
            elif op == 2:
                print("")
            else:
                print("Digite sim ou não\n")
    elif menu=="sair":
       print("Bye Bye!!")
    else:
       print("")