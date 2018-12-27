##---------------------------------------------------------------------------
class job:
    tempoChegada = 0
    picoCPU = 0
    tempoEspera = 0
    tempoResposta = 0
    tempoRetorno = 0
    executado = False

    def __init__(self, tempoChegada, picoCPU):
        self.tempoChegada = tempoChegada
        self.picoCPU = picoCPU

    def executa(self):
        self.picoCPU -= 1

    def espera(self):
        self.tempoEspera += 1

##---------------------------------------------------------------------------
def sortingPorChegada(jobArray):
    if not isinstance(jobArray, list):
        return None
    maxval = 0
    for i in jobArray:
        if i.tempoChegada > maxval:
            maxval = i.tempoChegada
    arraySize = len(jobArray)
    size2 = maxval + 1
    sorted = [''] * arraySize
    count = [0] * size2
    for j in jobArray:
        count[j.tempoChegada] += 1
    for i in range(1, size2):
        count[i] += count[i - 1]
    for n in range(arraySize - 1, -1, -1):
        count[jobArray[n].tempoChegada] -= 1
        sorted[count[jobArray[n].tempoChegada]] = jobArray[n]
    return sorted

##---------------------------------------------------------------------------
def sortingPorCPU(jobArray):
    if not isinstance(jobArray, list):
        return None
    if len(jobArray) == 0:
        return jobArray
    maxval = 0
    for i in jobArray:
        if i.picoCPU > maxval:
            maxval = i.picoCPU
    arraySize = len(jobArray)
    size2 = maxval + 1
    sorted = [''] * arraySize
    count = [0] * size2
    for j in jobArray:
        count[j.picoCPU] += 1
    for i in range(1, size2):
        count[i] += count[i - 1]
    for n in range(arraySize - 1, -1, -1):
        count[jobArray[n].picoCPU] -= 1
        sorted[count[jobArray[n].picoCPU]] = jobArray[n]
    return sorted

##---------------------------------------------------------------------------
def carregaFila(nome):
    retorno = [] #type: List(job)
    arq = open(nome, "r")
    for line in iter(lambda: arq.readline(), ''):
        line = line.strip('\n')
        line = line.split()
        line = [int(e) for e in line]
        tempo, pCpu = line
        retorno.append(job(tempo, pCpu))
    return retorno

##---------------------------------------------------------------------------
