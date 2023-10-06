import time
import os
import sqlite3
import matplotlib.pyplot as plt
from classes.pessoa import *
from classes.aviao import *

class Simulador:

    def criarBD(self):
        con = sqlite3.connect("simulacoes.db")
        cursor = con.cursor()
        cursor.execute('''
            CREATE TABLE simulacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                simulacao TEXT,
                tempo INTEGER
            )
        ''')
        con.commit()
        con.close()

    def pegarSimulacoesTestadas(self):
        '''
            retorna uma matriz com as simulações e o melhor tempo e sequência da tabela 
        '''
        
        if 'simulacoes.db' not in os.listdir():
            self.criarBD()

        con = sqlite3.connect("simulacoes.db")  
        cursor = con.cursor()
        cursor.execute('SELECT * FROM simulacoes')
        resultados = cursor.fetchall()

        simulacoes = []
        melhorSequencia = None
        melhorTempo = None

        for resultado in resultados:                                  # passa todas as sequencias da tabela para simulações

            if melhorTempo == None or resultado[2] < melhorTempo:     # obter melhor sequencia e melhor tempo de todas as simulações
                melhorTempo = resultado[2]
                melhorSequencia = resultado[1]

            simulacoes.append(resultado[1])

        con.close()

        matrixSimulacoes = []                                         
        for i in simulacoes:                                          # transforma a lista de strings em uma lista de listas
            sim = []
            for cada in i.split('_'):
                if cada != '':
                    sim.append(cada)
            matrixSimulacoes.append(sim)

        return {'matrix':matrixSimulacoes,'melhorTempo':melhorTempo,'melhorSequencia':melhorSequencia}

    def gerarGraficos(self):
        self.gerarGrafico(1)
        self.gerarGrafico()

    def gerarGrafico(self, opcao=0):
        '''
            opcao 1 = gera uma gráfico da taxa de variação do tempo pela quantidade de simulações
            outra opcao = gera um gráfico do resultado da simulação
        '''

        x = []      # lista de tempo
        y = []      # lista de quantidade de simulações

        con = sqlite3.connect("simulacoes.db")
        cursor = con.cursor()

        if opcao==1:                                        # tabela é ordenada pelas simulações de maior tempo ao menor
            cursor.execute('SELECT * FROM simulacoes ORDER BY tempo DESC')
        else:                                               # tabela não é ordenada
            cursor.execute('SELECT * FROM simulacoes')

        resultados = cursor.fetchall()
        melhorTempo = None

        ultima = None

        for i, resultado in enumerate(resultados):    
            # gera a listas que serão usadas para criar o grafico, 
            # adicionando o tempo e quantidade de simulações nas listas a cada 100 simulaçoes, se o tempo for diferente do ultimo

            if i % 100 == 0:        
                if melhorTempo != ultima or ultima==None:
                    x.append(i)
                    y.append(melhorTempo)
                    ultima = melhorTempo

            if melhorTempo == None:
                melhorTempo = resultado[2]
            
            elif resultado[2] < melhorTempo:
                melhorTempo = resultado[2]
            
        con.close()

        plt.plot(x, y, color='black', linestyle='solid', linewidth=1)
        plt.title('Gráfico de Tempo de Embarque')
        plt.xlabel('Quantidade de Simulações')
        plt.ylabel('Tempo')

        if opcao==1:
             plt.savefig('graficos/graficoTaxaDeVariacao.png')
        else:
             plt.savefig('graficos/grafico.png')

        plt.show()
            
    def rodarSimulacoes(self, quantidadeSimulacoes, opcao, qtdAssento, qtdColuna):
        '''
            Faz n simulações de embarque de passageiros no avião
            opcao: exibir entrada dos aviões
        '''

        if qtdAssento%qtdColuna!=0:  
            print("Argumetos incorretos.")
            return
        
        sequencias = self.pegarSimulacoesTestadas()
        sequenciasTestadas = sequencias['matrix']
        melhorSequencia = sequencias['melhorSequencia']
        melhorTempo = sequencias['melhorTempo']
        
        con = sqlite3.connect("simulacoes.db")
        cursor = con.cursor()
        
        for index,i in enumerate(range(quantidadeSimulacoes)):

            aviao = Aviao(qtdAssento, qtdColuna) 

            filaDeEmbarque = []
            sequencia = [] 
            
            while True:   # gera fila de embarque com uma sequencia não existe no banco de dados
                
                filaDeEmbarque = []
                sequencia = []
                posicoes = []

                for i in aviao.coluna:      # gera as posições possiveis dos assentos
                    for numero in range(1,aviao.classes[0].numFileiras+1):
                        posicoes.append(f'{i}{numero}')
                
                while posicoes != []:      # metodo aleatorio para a ordem dos passageiros na fila de embarque

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
                        print(f'simulação: {index + 1} de {quantidadeSimulacoes}')
                        print('melhor tempo:',melhorTempo)
                        print('faltando embarcar:',len(filaDeEmbarque))
                        print('tempo:',tempo)
                        print(aviao)

            if melhorTempo == None or tempo < melhorTempo:       # define o melhor tempo testado
                melhorTempo = tempo
                melhorSequencia = sequencia

            sequenciasTestadas.append(sequencia)
            
            stringSequencia = ''
            for cada in sequencia:
                stringSequencia += cada + '_'
            
            cursor.execute('INSERT INTO simulacoes (simulacao, tempo) VALUES (?, ?)', (stringSequencia,tempo))
                
        print('melhor sequencia:',melhorSequencia)
        print('melhorTempo:',melhorTempo)

        con.commit()
        con.close()

        self.gerarGraficos()
    
