import settings
def aloca_mem(job, position):
    settings.memory_space[position:position + job.memoryReq] = [job.name] * job.memoryReq

def desaloca_mem(job):
    settings.memory_space[job.memPosition:job.memPosition + job.memoryReq] = [0] * job.memoryReq

def getMultProgram():
    varMult = input("Deseja multiprogramação? (s/n) \n")
    if (varMult == "n"):
        return 1
    elif (varMult == "s"):
        return input("Escolha o grau de multiprogramação: ")


def getTypeProcess():
    print("\nPrioridade de Processamento:")
    print("1 - FIFO")
    print("2 - Jobs mais curtos")
    varProcess = input("Escolha o tipo de administracao de processamento: ")
    return varProcess


def getTypeMemory():
    print("\nTipos de Alocação de Memória:")
    print("1 - Alocação Contígua Simples")
    print("2 - Memória particionada, Worst-fit")
    print("3 - Memória particionada, First-fit")
    # print("3 - Overlay:")
    varMemory = input("Escolha o tipo de administracao de processamento: ")
    return varMemory

def printaProc():
    print("number_of_processors: ", settings.number_of_processors, settings.time)
