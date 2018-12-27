import copy

#----------- Preparação ---------------

try:
    #Abrindo arquivo
    arq = open("dados.txt", "r")
except IOError:
    print("Arquivo não existente!")
    exit(-1)
#quantidade de quadros
quadrosQuantidade = int(arq.readline())
quadros = []

#As consultas dos quadros na ordem de chegada
consultas = []
#Preenchendo as consultas
for num in iter(lambda: arq.readline(), ''):
    consultas.append(int(num))
#Contagem de faltas
faltas = 0
#------------------------------ FIFO ------------------------
for i in consultas:
    if i not in quadros:
        faltas += 1
        if len(quadros) < quadrosQuantidade:
            quadros.insert(0, i)
        else:
            quadros.pop()
            quadros.insert(0, i)
print("FIFO", faltas)
#----------------------------- Ótimo ------------------------
faltas = 0
quadros = []
for i in range(0, len(consultas)):
    if consultas[i] not in quadros:
        faltas += 1
        if len(quadros) < quadrosQuantidade:
            quadros.insert(0, consultas[i])
        else:
            atual = 0
            ocorrenciaAtual = 0
            try:
                for j in quadros:
                    ocorrencia = consultas[i+1:len(consultas)].index(j)
                    if ocorrencia > ocorrenciaAtual:
                        atual = j
                        ocorrenciaAtual = ocorrencia
                quadros.pop(quadros.index(atual))
                quadros.insert(0, consultas[i])
            except ValueError:
                quadros.pop()
                quadros.insert(0, i)
print("OTM", faltas)
del ocorrenciaAtual
del ocorrencia
del atual
del j

#------------------------------ LRU -------------------------
faltas = 0
quadros = []
#Vetor para contagem do tempo de cada quadro
#Já inicializado com zeros, na mesma quantidade que o vetor de quadros
tempo = [0] * len(quadros)

for i in consultas:
    if i not in quadros:
        faltas += 1
        if len(quadros) < quadrosQuantidade:
            quadros.insert(0, i)
        else:
            quadros.pop()
            quadros.insert(0, i)
    else:
        quadros.insert(0, quadros.pop(quadros.index(i)))

print("LRU", faltas)

