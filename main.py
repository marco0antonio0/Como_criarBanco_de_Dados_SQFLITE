from datetime import datetime
import time
from selenium import webdriver
from funcoes.enviar_msg import enviarMensagem
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class whats:
    def __init__(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument('lang=pt-br')
        opt.add_argument('user-data-dir=./dados_salvar')
        opt.headless = False
        opt.add_argument("start-maximized")
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
    def enviar_por_horario(self,contato,horario,mensagem):
        data = datetime.now()
        hora = data.strftime('%H:%M')
        if hora == horario:
            enviarMensagem(driver=self.driver, contato=contato,mensagem=mensagem, opcao=1)
            time.sleep(1)
            self.driver.refresh()
            time.sleep(20)




iniciar_bot = whats()
iniciar_bot.abrirWhatsapp()
# ======================================================================================
#                           inicio do loop
#
# ======================================================================================
while True:
    
    # print(data.strftime('%H:%M:%S'))


    # ======================================================================================
    #                         Enviar MGS por horarios
    # ======================================================================================

    horario='17:51'
    mensagem='Esta é uma mensagem automatica\nOla sou Bot capivara, estou aprendendo a me comunicar por comando de horarios\npassou 1'
    contato='Marco Antonio'
    iniciar_bot.enviar_por_horario(horario =horario,contato=contato,mensagem = mensagem)
    
    # ======================================================================================
    
    horario='17:52'
    mensagem='passou 2'
    contato='Marco Antonio'
    iniciar_bot.enviar_por_horario(horario =horario,contato=contato,mensagem = mensagem)
   
    # ======================================================================================

   
   
   
   
   
   
   
   
   
   
   
   
   
   
    time.sleep(30)

 

