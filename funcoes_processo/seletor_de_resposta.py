from funcoes_processo.validacao.validade import forms
from datetime import datetime
data = datetime.now()
apenas_hora = int(data.strftime('%H'))
if apenas_hora >= 6 and apenas_hora < 12:
    msg1 = 'bom dia'
if apenas_hora >= 12 and apenas_hora < 17:
    msg1 = 'boa tarde'
if apenas_hora >= 17 and apenas_hora <= 23:
    msg1 = 'boa noite'
if apenas_hora >= 0 and apenas_hora < 6:
    msg1 = 'boa noite'

menu = """
{} cliente, temos :
[1] <-- coca cola 2L
[2] <-- tapioca
[3] <-- cafe
""".format(msg1)


def passarEtapa(nome, etapa):
    etapasContatos.pop()
    etapasContatos.append([nome, etapa])
    status_ = False
    print(etapasContatos)
    return status_
# etapasContatos[id][nome,etapa]
# etapasContatos[id][ 0,  1 ]


etapasContatos = []


def seletor_de_eventos(nome_contato, msg):

    msg = msg.lower()
    status = True
    # ============================================
    #         Varrer Lista
    for i in range(0, len(etapasContatos)):
        # ==========================================
        #       Procurar nome na lsita
        if nome_contato == etapasContatos[i][0]:
            # ========================================
            #     Etapa 1
            if 1 == etapasContatos[i][1]:
                etapa = etapasContatos[i][1]+1
                nome = etapasContatos[i][0]
                # dados[ textBase,status ]
                pergunta_1 = forms(msg_cliente=msg, dic=[
                                   'inicia', 'iniciar', 'inicio', '1'], status=True)
                pergunta_2 = forms(msg_cliente=msg, dic=[
                                   'sai', 'sair', 's', '2'], status=True)
                if pergunta_1:
                    mensagem = 'Voce escolheu entrar'
                    status = passarEtapa(nome=nome, etapa=etapa)
                    return mensagem
                if pergunta_2:
                    mensagem = 'Voce escolheu sair'
                    status = passarEtapa(nome=nome, etapa=1)
                    return mensagem

                if not pergunta_1 and not pergunta_2:
                    mensagem = 'resposta invalida\nselecione uma resposta' + \
                        '\nola,boa tarde\n-1- iniciar\n-2- sair'
                    return mensagem

            # ========================================
            #     Etapa 2
            if 2 == etapasContatos[i][1]:
                etapa = etapasContatos[i][1]+1
                nome = etapasContatos[i][0]
                pergunta_1 = forms(dic=[''])
                status = passarEtapa(nome=nome, etapa=etapa)

            # ========================================
            #     Etapa 3
            if 3 == etapasContatos[i][1]:
                etapa = etapasContatos[i][1]+1
                nome = etapasContatos[i][0]
                status = passarEtapa(nome=nome, etapa=etapa)
            if 3 < etapasContatos[i][1]:
                status = False
                print('etapas d++')
                break

    if status:
        nome = nome_contato
        etapa = 1
        etapasContatos.append([nome, etapa])
        mensagem = menu
        return mensagem
