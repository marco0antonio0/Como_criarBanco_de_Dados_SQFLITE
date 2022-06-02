from funcoes_processo.validacao.pergunta_1 import pergunta_1
from funcoes_processo.validacao.pergunta_2 import pergunta_2


def processamento(msg,etapa):
    if etapa == 1:  
        return  pergunta_1()
    
    if etapa == 2:  
        return  pergunta_2()
    
    if etapa == 3:  
        return  pergunta_2()

    if etapa == 4:  
        return  pergunta_2()