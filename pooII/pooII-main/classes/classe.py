import random

class Classe:

    def __init__(self,nome, qtdAssento, qtdColunas):
        self.nomeClasse = nome
        self.assentos = []
        self.assentosDisponiveis = []
        self.lotada = False

        self.quantidadeAssentos =  qtdAssento # recebem do simulador
        self.assentosPorColuna = qtdColunas  #numDeColunas
        self.numFileiras = int(self.quantidadeAssentos/self.assentosPorColuna)

    def ocuparAssento(self,passageiro,numero = None):

        if self.assentosDisponiveis == []:
            self.lotada = True
            return

        if numero == None:
            numero = random.choice(self.assentosDisponiveis)

        for assento in self.assentos:
            if assento.numero == numero:
                assento.ocuparAssento(passageiro)

        self.assentosDisponiveis.remove(numero)
