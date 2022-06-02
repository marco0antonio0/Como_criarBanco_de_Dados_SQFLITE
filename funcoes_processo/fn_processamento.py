from funcoes_processo.validacao.pergunta_1 import pergunta_1
from funcoes_processo.validacao.pergunta_2 import pergunta_2


def processamento(msg='',etapa =0):
    if etapa == 0 or etapa == 1 or etapa == 2 or etapa == 3 or etapa == 4  :
        if etapa == 0:  
            return  pergunta_1()
        if etapa == 1:  
            return  pergunta_2()
        
        if etapa == 2:  
            return  pergunta_2()
        
        if etapa == 3:  
            return  pergunta_2()

        if etapa == 4:  
            return  pergunta_2()
    else:
        return 'nada'
