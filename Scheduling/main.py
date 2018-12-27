import FuncoesClasses
import copy
from decimal import Decimal

arquivo = "data.txt"

fila = FuncoesClasses.carregaFila(arquivo)
fila = FuncoesClasses.sortingPorChegada(fila)
"""Iniciando o processamento
Basicamente: loop farão a contagem temporal
O jobs em execução terá seu ciclo de CPU diminuido
os jobs em espera terão o tempo de espera incrementado
ao final, as medias sao calculadas
    tempoChegada
    picoCPU
    tempoEspera
    tempoResposta
    tempoRetorno
    Tempo de retorno: tempo desde a primeira execução até o final do processo
    Tempo de resposta: Tempo até a primeira execução do processo
    Tempo de Espera: espera
"""
"""-------------------FCFS-------------------------------------------------------------------------"""
filaFCFS = copy.deepcopy(fila)
filaFCFSProntos = [] #type: List(job)
Concluidos = 0
inicio = 0
while Concluidos < len(filaFCFS):
    while inicio < len(filaFCFS) and filaFCFS[inicio].tempoChegada == 0:
        filaFCFSProntos.append(filaFCFS[inicio])
        inicio += 1
    for jfcfs in filaFCFS:
        if jfcfs.tempoChegada > 0:
            jfcfs.tempoChegada -= 1
    if len(filaFCFSProntos) > 0:
        for Job in filaFCFSProntos:
            Job.tempoRetorno += 1
            if Job is not filaFCFSProntos[0]:
                Job.tempoEspera += 1
        filaFCFSProntos[0].executado = True
        filaFCFSProntos[0].picoCPU -= 1
        if filaFCFSProntos[0].picoCPU == 0:
            filaFCFSProntos.pop(0)
            Concluidos += 1
        for Job in filaFCFSProntos:
            if not Job.executado:
                Job.tempoResposta += 1

totalEspera = 0.0
totalRetorno = 0.0
totalResposta = 0.0
for i in filaFCFS:
    totalEspera += i.tempoEspera
    totalResposta += i.tempoResposta
    totalRetorno +=  i.tempoRetorno
x = Decimal(totalEspera / len(fila))
totalEspera = round(x, 1)
x = Decimal(totalResposta / len(fila))
totalResposta = round(x, 1)
x = Decimal(totalRetorno / len(fila))
totalRetorno = round(x, 1)
print("FCFS", totalRetorno, totalResposta, totalEspera)
del(filaFCFS)
del(filaFCFSProntos)
"""-------------------SJF-------------------------------------------------------------------------"""

filaSJF = copy.deepcopy(fila)
filaSJFProntos = [] #type: List(job)
Concluidos = 0
inicio = 0
ordenar = True
while Concluidos < len(filaSJF):
    while inicio < len(filaSJF) and filaSJF[inicio].tempoChegada == 0:
        filaSJFProntos.append(filaSJF[inicio])
        inicio += 1
    if ordenar and len(filaSJFProntos) > 0:
        ordenar = False
        filaSJFProntos = FuncoesClasses.sortingPorCPU(filaSJFProntos)
    for jSJF in filaSJF:
        if jSJF.tempoChegada > 0:
            jSJF.tempoChegada -= 1

    if len(filaSJFProntos) > 0:
        for numJob in filaSJFProntos:
            numJob.tempoRetorno += 1
            if numJob is not filaSJFProntos[0]:
                numJob.tempoEspera += 1
        filaSJFProntos[0].executado = True
        filaSJFProntos[0].picoCPU -= 1
        if filaSJFProntos[0].picoCPU == 0:
            filaSJFProntos.pop(0)
            Concluidos += 1
            ordenar = True
        for Job in filaSJFProntos:
            if not Job.executado:
                Job.tempoResposta += 1

totalEspera = 0.0
totalRetorno = 0.0
totalResposta = 0.0
for i in filaSJF:
    totalEspera += i.tempoEspera
    totalResposta +=  i.tempoResposta
    totalRetorno += i.tempoRetorno
x = Decimal(totalEspera / len(fila))
totalEspera = round(x, 1)
x = Decimal(totalResposta / len(fila))
totalResposta = round(x, 1)
x = Decimal(totalRetorno / len(fila))
totalRetorno = round(x, 1)
print("SJF", totalRetorno, totalResposta, totalEspera)
del(filaSJF)
del(filaSJFProntos)
del(ordenar)
"""-------------------RR-------------------------------------------------------------------------"""

filaRR = copy.deepcopy(fila)
filaRRProntos = [] #type: List(job)
Concluidos = 0
inicio = 0
robin = 0
ultimoFinalizou = False

while Concluidos < len(filaRR):
    while inicio < len(filaRR) and filaRR[inicio].tempoChegada == 0:
        filaRRProntos.append(filaRR[inicio])
        inicio += 1
    if len(filaRRProntos) > 0 and robin == 2:
        robin = 0
        filaRRProntos.append(filaRRProntos.pop(0))
    if len(filaRRProntos)>0:
        robin += 1
    for jo in filaRR:
        if jo.tempoChegada > 0:
            jo.tempoChegada -= 1
    if len(filaRRProntos) > 0:
        for jo in filaRRProntos:
            jo.tempoRetorno += 1
            if jo is not filaRRProntos[0]:
                jo.tempoEspera += 1
        filaRRProntos[0].picoCPU -= 1
        filaRRProntos[0].executado = True
        if filaRRProntos[0].picoCPU == 0:
            filaRRProntos.pop(0)
            robin = 0
            Concluidos += 1
        for jo in filaRRProntos:
            if not jo.executado:
                jo.tempoResposta += 1



totalEspera = 0.0
totalRetorno = 0.0
totalResposta = 0.0
for i in filaRR:
    totalEspera += i.tempoEspera
    totalRetorno += i.tempoRetorno
    totalResposta += i.tempoResposta
x = Decimal(totalEspera / len(fila))
totalEspera = round(x, 1)
x = Decimal(totalResposta / len(fila))
totalResposta = round(x, 1)
x = Decimal(totalRetorno / len(fila))
totalRetorno = round(x, 1)
print("RR ", totalRetorno, totalResposta, totalEspera)