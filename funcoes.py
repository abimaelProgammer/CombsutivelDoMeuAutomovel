class Carro:
    def __init__(self, consumo):
        self.combustivel = 0
        self.consumo = 1.0 / consumo
        self.capacidade = 100

    def andar(self, distancia):
        if self.combustivel >= distancia * self.consumo:
            self.combustivel -= distancia * self.consumo
            print("Vruuum!!")
        else:
            print("Gasolina insuficiente para fazer a viagem")

    def obterGasolina(self):
        print("Gasolina:", int(self.combustivel), "L")

    def adicionarGasolina(self, litros):

        if self.combustivel + litros <= self.capacidade:
            self.combustivel += litros
        else:
            self.combustivel = self.capacidade
            print("Tanque cheio Sobrou ", (litros - self.capacidade), "L")
def simOuNao(op):
       if op == "sim" or op=="Sim" or op=="SIM" or op=="yes" or op=="Yes" or op=="YES":
           op=int(1)
           return op
       elif op=="nao" or op=="Nao" or op=="NAO" or op=="não" or op=="Não" or op=="NÃO" or op=="no" or op=="No" or op=="NO":
           op= int(2)
           return op
       else :
           return 'null'