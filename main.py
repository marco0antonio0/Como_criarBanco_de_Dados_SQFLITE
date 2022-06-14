from datetime import datetime
from distutils.command.config import config
import time
from selenium import webdriver
from funcoes.enviar_msg import enviarMensagem
from funcoes.varredura_contato import varreduras_de_contatos
from funcoes.varredura_msg import varredura_msg
from funcoes.varredura_notify import varreduras_de_notificacao
from funcoes_processo.seletor_de_resposta import seletor_de_eventos
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class whats:
    def __init__(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument('lang=pt-br')
        opt.add_argument('user-data-dir=./dados_salvar')
        opt.headless = False
        #self.driver = webdriver.Chrome(executable_path='./dados_navegador/chromedriver', options=opt)

        self.driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=opt)
        # self.driver.get("https://www.google.com")
    # =============================================================

    def abrirWhatsapp(self):
        self.driver.get('https://web.whatsapp.com')
    # =============================================================

    def atualizar(self):
        self.driver.refresh()
    # =============================================================
    # parametros{especificar a mensagem, nome do contato}

    def enviar_msg_base(self, contato, mensagem, opcao):
        enviarMensagem(driver=self.driver, contato=contato,
                       mensagem=mensagem, opcao=opcao)
    # =============================================================
    # retorna as mensagens selecionadas

    def varredura_msg_base(self, contato):
        selecionar_msg = varredura_msg(driver=self.driver, contato=contato)
        return selecionar_msg
    # =============================================================

    def varreduras_de_contatos_base(self):
        varreduras_de_contatos(driver=self.driver)
    # =============================================================
    # retorna  'dados'  =>>> sequecia [posição,nome de usuario,qtd notificação]

    def varreduras_de_notificacao_base(self):
        dados = varreduras_de_notificacao(driver=self.driver)
        return dados
    # =============================================================


iniciar_bot = whats()
iniciar_bot.abrirWhatsapp()
# ======================================================================================
#                           inicio do loop
#
# ======================================================================================
operar = False
esta_procurando_ainda = True
japrintei = True
dados = ''
while True:
    # print(data.strftime('%H:%M:%S'))
    data = datetime.now()
    hora = data.strftime('%H:%M')

    # =======================================================
    #           Loop de verificação e validação
    # =======================================================
    if operar:
        dados = iniciar_bot.varreduras_de_notificacao_base()
        if len(dados) > 0:
            for i in range(len(dados)):
                # dados[ posiçao_na_lista ][ id, nome, qtd_notificação]
                lista_mensagens = iniciar_bot.varredura_msg_base(
                    contato=dados[i][1])
                resposta = seletor_de_eventos(nome_contato=dados[i][1], msg=(
                    lista_mensagens[(len(lista_mensagens)-1)].text))
                iniciar_bot.enviar_msg_base(
                    contato=dados[i][1], mensagem=resposta, opcao=2)
                print('passei')
                time.sleep(1)
                iniciar_bot.atualizar()
                japrintei = True

    # ======================================================================================
    #
    #

    # ======================================================================================
    #                         Enviar MGS por horarios
    # ======================================================================================

    if hora == '13:27' or True:
        iniciar_bot.atualizar()
        iniciar_bot.enviar_msg_base(opcao=1,
                                    mensagem=f'ola marco são extamente --> {hora}', contato='Marco Antônio')
    # ======================================================================================
    #                                'Procurando'
    # ======================================================================================
    if len(dados) == 0:
        time.sleep(3)
        if esta_procurando_ainda and japrintei:
            print('\n\n')
            print('================================')
            print('   Procurando Mensagens......')
            print('================================')
            print('\n')
            japrintei = False
