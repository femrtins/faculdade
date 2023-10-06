sequencia = []
posicoes = []
coluna = ['A', 'B','C','D','E','F']
fileiras = 6
for i in coluna:                       
    for numero in range(1,fileiras+1):
        posicoes.append(f'{i}{numero}')

print(posicoes)

while posicoes!=[]:

    lim = fileiras//2

    for n in range(1,(fileiras - lim) +1):
        sequencia.append(posicoes[len(posicoes) - n])
        del posicoes[len(posicoes)- n]

    if len(posicoes)!=fileiras:
        for n in range(1,fileiras+1, 2):
            sequencia.append(posicoes[fileiras-n]) 
            del posicoes[fileiras-n]     
 
    for n in range(1, lim + 1):
        sequencia.append(posicoes[len(posicoes) - 1])
        del posicoes[len(posicoes) - 1]

    if len(posicoes)!=fileiras:
        for n in range(lim -1, -1, -1):
            sequencia.append(posicoes[fileiras-fileiras+n])
            del posicoes[fileiras-fileiras+ n]
        
print(sequencia)