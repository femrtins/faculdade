from classes.classe import *
from classes.assento import *

class Aviao:
    
    classesDisponiveis = ["Classe Economica"]

    def __init__(self, qtdAssentos, qtdColunas):
        
        self.classes = []

        self.coluna = []

        ini = 65
        while ini-65!= qtdColunas:          # gera uma lista representando as colunas do avião
            self.coluna.append(chr(ini))
            ini+=1

        for classe in self.classesDisponiveis:      # cria a classe com os assentos
            
            x = 0   # determina a  coluna 
            y = 1   # determina a fileira
            classObj = Classe(classe, qtdAssentos, qtdColunas)
            
            for assento in range(classObj.quantidadeAssentos):  # para cada assento sera atribuido um numero
                
                numeroAssento = f'{self.coluna[x]}{y}'          
                x += 1
                if(x == len(self.coluna)):                      # fileira n está completa
                    x = 0
                    y += 1

                classObj.assentosDisponiveis.append(numeroAssento)
                classObj.assentos.append(Assento(numeroAssento))
            
            self.classes.append(classObj)
        
        self.corredor = []
        for i in range( self.classes[0].numFileiras ):
            self.corredor.append(None)

    def corredorVazio(self):
        for i in self.corredor:
            if i !=None:
                return False
        return True
            
        
    def colocarfila(self, passageiro):
        if self.corredor[0]==None:
            self.corredor[0] = passageiro
            return True
        else:
            return False
    
    def andarFila(self):
        
        for index, passageiro in enumerate(reversed(self.corredor)):

            if passageiro==None:
                continue

            posicao = len(self.corredor)-1 - index

            if posicao+1 == passageiro.numFila:
                if not passageiro.tempoBagagem or not passageiro.temBagagem:
                    self.classes[0].ocuparAssento( passageiro = passageiro , numero = passageiro.assento)
                    self.corredor[posicao] = None
                    passageiro.colocandoBagagem = False
                    continue
                else:
                    passageiro.tempoBagagem-=1
                    passageiro.colocandoBagagem = True
                    continue
   
            if posicao >= len(self.corredor)-1:
                continue

            if self.corredor[posicao+1] == None:
                self.corredor[posicao+1], self.corredor[posicao] = self.corredor[posicao], self.corredor[posicao+1]
    

    def __str__(self):
        string = ''

        for classe in self.classes:
            string += f'\n[---AVIÃO---]'

            cont = 1
            string+= f"\n\n    "
            for i in self.coluna:   #string += f'\n\n    [A. ][B. ][C. ] |      | [D. ][E. ][F. ]'
                string+= f'[{i}. ]'
                if cont == int( classe.assentosPorColuna / 2 ):
                    string+= f" |      | "
                cont+=1

            contador = 0
            x = 1   # numero da coluna
            y = 1   # numero da fila
            for assento in classe.assentos: 
                if x == 1:
                    if y<10:
                        string += f'\n 0{y} '
                    else:
                        string += f'\n {y} '
                if assento.ocupado:
                    string += f'<0{assento.passageiro.ordemEntrada}>'
                else:
                    if int(assento.numero[1:])<10:
                        string += f'[{assento.numero[:1]}0{assento.numero[1:]}]'
                    else:
                        string += f'[{assento.numero}]'

                contador += 1
                if contador == int( classe.assentosPorColuna / 2 ):
                    if self.corredor[y-1]!=None:
                        if self.corredor[y-1].temBagagem:
                            if self.corredor[y-1].colocandoBagagem:
                                string += f' |  {self.corredor[y-1].ordemEntrada}- | '
                            else:
                                string += f' |  {self.corredor[y-1].ordemEntrada}+ | '
                        else:
                            string += f' |  {self.corredor[y-1].ordemEntrada}  | '
                    else:
                        string += f' | {self.corredor[y-1]} | '
                x += 1
                if contador == classe.assentosPorColuna:
                    contador = 0
                    y += 1
                    x = 1
            return string
