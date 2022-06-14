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
    # =============================================================

    def abrirWhatsapp(self):
        self.driver.get('https://web.whatsapp.com')
    # =============================================================

    def atualizar(self):
        self.driver.refresh()
    # =============================================================
    # parametros{especificar a mensagem, nome do contato}

    def enviar_msg_base(self, contato, mensagem, opcao):
        enviarMensagem(driver=self.driver, contato=contato,mensagem=mensagem, opcao=opcao)
    # =============================================================



iniciar_bot = whats()
iniciar_bot.abrirWhatsapp()
# ======================================================================================
#                           inicio do loop
#
# ======================================================================================
while True:
    # print(data.strftime('%H:%M:%S'))
    data = datetime.now()
    hora = data.strftime('%H:%M')

    # ======================================================================================
    #                         Enviar MGS por horarios
    # ======================================================================================

    if hora == '13:27':
        iniciar_bot.enviar_msg_base(opcao=1,mensagem=f'ola marco são extamente --> {hora}', contato='Marco Antonio')
        iniciar_bot.atualizar()
    # ======================================================================================

 
