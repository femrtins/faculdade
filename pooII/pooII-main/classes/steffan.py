import time
import os
import sqlite3
import matplotlib.pyplot as plt
from classes.pessoa import *
from classes.aviao import *

def simulacaoSteffan(self, opcao, qtdAssento, qtdColuna):
        '''
            Faz n simulações de embarque de passageiros no avião
            opcao: exibir entrada dos aviões
        '''

        if qtdAssento%qtdColuna!=0:  
            print("Argumetos incorretos.")
            return
        
        sequencias = self.pegarSimulacoesTestadas()
        #sequenciasTestadas = sequencias['matrix']
        sequenciasTestadas = []
        melhorSequencia = sequencias['melhorSequencia']
        melhorTempo = sequencias['melhorTempo']

        print('melhor sequencia aletoria:',melhorSequencia)
        print('melhorTempo aleatorio:',melhorTempo)

        sequenciasTestadas.append(melhorSequencia)
        
        #con = sqlite3.connect("simulacoes.db")
        #cursor = con.cursor()
        
        #for index,i in enumerate(range(quantidadeSimulacoes)):

        aviao = Aviao(qtdAssento, qtdColuna) 

        filaDeEmbarque = []
        sequencia = [] 
        
        while True:   # gera fila de embarque com uma sequencia não existe no banco de dados
            
            filaDeEmbarque = []
            sequencia = []
            posicoes = []

            for i in aviao.coluna:                # gera as posições possiveis dos assentos
                for numero in range(1,aviao.classes[0].numFileiras+1):
                    posicoes.append(f'{i}{numero}')
            
            while posicoes != []:                # metodo aleatorio para a ordem dos passageiros na fila de embarque

                posicao = random.choice(posicoes)
                filaDeEmbarque.append(Adulto('nome',posicao))
                sequencia.append(posicao)
                posicoes.remove(posicao)
                
            if filaDeEmbarque not in sequenciasTestadas:  
                sequenciasTestadas.append(filaDeEmbarque)
                break
        
        tempo = 0
        contadorEntrada = 0

        for _ in aviao.classes:

            while filaDeEmbarque != [] or not aviao.corredorVazio():  # colocar as pessoas da fila de embarque em seus respectivos assentos

                aviao.andarFila()
                
                ordem = ''

                if(contadorEntrada < 10):                            # definir a ordem de entrada de cada passageiro que entra no corredor
                    ordem = '0' + str(contadorEntrada)  
                else:
                    ordem = str(contadorEntrada)
                
                if filaDeEmbarque != []:                             # o passageiro entra no corredor se ainda tem alguem na fila de embarque
                    passageiro = filaDeEmbarque[0]
                    passageiro.ordemEntrada = ordem

                    if aviao.colocarfila(passageiro):                # coloca o passageiro no corredor e o tira da fila de embarque
                        filaDeEmbarque.pop(0)    
                        contadorEntrada += 1    
                
                tempo += 1                                   
                
                if opcao:                                 
                    time.sleep(0.1)
                    os.system('cls')
                    print(f'simulação metodo Steffan')
                    print('faltando embarcar:',len(filaDeEmbarque))
                    print('tempo:',tempo)
                    print(aviao)

        if melhorTempo == None or tempo < melhorTempo:       # define o melhor tempo testado
            melhorTempo = tempo
            melhorSequencia = sequencia

        #sequenciasTestadas.append(sequencia)
        
        #stringSequencia = ''
        #for cada in sequencia:
        #    stringSequencia += cada + '_'
        
        #cursor.execute('INSERT INTO simulacoes (simulacao, tempo) VALUES (?, ?)', (stringSequencia,tempo))
            
        print('melhor sequencia:',melhorSequencia)
        print('melhorTempo:',melhorTempo)

        #con.commit()
        #con.close()

        #self.gerarGraficos()