from ProcessoP import Processo, coletarProcessos


def cmp(p: Processo):
    return p.cpu


def topprocessos():
    """ Retorna os 5 processos que mais consomem memória """

    processos = coletarProcessos()
    processos.sort(reverse=True, key=cmp)
    print(processos[:5])
    return processos[:5]


topprocessos()
