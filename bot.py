from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

lista_msg = []
class whats:
    def __init__(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument('lang=pt-br')
        opt.add_argument('user-data-dir=\dados')
        opt.headless = False
        opt.add_argument("start-maximized")
        #self.driver = webdriver.Chrome(executable_path='./dados_navegador/chromedriver', options=opt)

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
    # =============================================================
    #   abre o site - 'https://web.whatsapp.com/'
    def abrirWhatsapp(self):
        self.driver.get('https://web.whatsapp.com/')
    # =============================================================
    #   atualiza a pagina atual
    def atualizar(self):
        self.driver.refresh()
    # =============================================================
    # parametros{especificar a mensagem, nome do contato}
    def send(self,contato,mensagem):
        driver = self.driver
        while True:
            try:
                pesquisar = driver.find_element(By.CSS_SELECTOR,'div[title="Caixa de texto de pesquisa"]')
                if pesquisar != None:
                    break
            except:
                pass
        pesquisar.click()
        pesquisar.send_keys(f'{contato}')
        time.sleep(2)
        while True:
            try:
                contato_ = driver.find_element(By.CSS_SELECTOR,f'span[title="{contato}"]')
                break
            except:
                pass
        contato_.click()
        while True:
            try:
                mensagem_ = driver.find_element(By.CSS_SELECTOR,'div[title="Mensagem"]')
                break
            except:
                pass
        mensagem_.send_keys(f'{mensagem}')
        while True:
            try:
                btn_send = driver.find_element(By.CSS_SELECTOR,'span[data-icon="send"]')
                break
            except:
                pass
        btn_send.click()
        time.sleep(2)
    #ler mensagem de um contato especifico e retorna-la
    def read(self,contato):
        driver = self.driver
        while True:
            try:
                pesquisar = driver.find_element(By.CSS_SELECTOR,'div[title="Caixa de texto de pesquisa"]')
                if pesquisar != None:
                    break
            except:
                pass
        pesquisar.click()
        pesquisar.send_keys(f'{contato}')
        time.sleep(2)
        while True:
            try:
                contato_ = driver.find_element(By.CSS_SELECTOR,f'span[title="{contato}"]')
                break
            except:
                pass
        contato_.click()
        time.sleep(5)
        read_msg = driver.find_elements(By.CSS_SELECTOR,'div[role="row"]')
        for linha in read_msg:
            lista_msg.append(linha.text)
        return lista_msg

 


