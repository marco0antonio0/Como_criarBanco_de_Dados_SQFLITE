import time
from datetime import datetime

def pergunta_1():
    data = datetime.now()
    #hora = data.strftime('%H:%M')
    apenas_hora = data.strftime('%H')
    apenas_hora = int(apenas_hora)
    if apenas_hora >=6 and apenas_hora<12:
        msg1 = 'bom dia'
    if apenas_hora >=12 and apenas_hora<17:
        msg1 = 'boa tarde'
    if apenas_hora >=17 and apenas_hora<=23:
        msg1 = 'boa noite'
    if apenas_hora >=0 and apenas_hora<6:
        msg1 = 'boa noite'
    
    textBase = f"""
    {msg1}
    nossas opções:
    2- horario de aula semanal
    3- mandar mensagem para raquel
    1- mandar mensagem para craudio
    """
    return textBase