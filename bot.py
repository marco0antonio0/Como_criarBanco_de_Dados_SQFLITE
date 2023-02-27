from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

lista_msg = []


class Bot:
    def __init__(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument('lang=pt-br')
        opt.add_argument('user-data-dir=\dados')
        opt.headless = False
        opt.add_argument("start-maximized")
        # self.driver = webdriver.Chrome(executable_path='./dados_navegador/chromedriver', options=opt)

        self.driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=opt)
    # =============================================================
    #   abre o site - 'https://web.whatsapp.com/'

    def abrirWhatsapp(self):
        self.driver.get('https://web.whatsapp.com/')
    # =============================================================
    #   atualiza a pagina atual

    def atualizar(self):
        self.driver.refresh()
    # =============================================================
    #   Verificar se a pagina esta carregada

    def IsLoadSearch(self):
        while True:
            try:
                pesquisar = self.driver.find_element(
                    By.CSS_SELECTOR, 'div[title="Caixa de texto de pesquisa"]')
                if pesquisar != None:
                    return pesquisar
            except:
                pass
    # =============================================================

    def findElement_Select(self, args):
        #  By.CSS_SELECTOR
        while True:
            try:
                args_ = self.driver.find_element(By.CSS_SELECTOR, args)
                if args_ != None:
                    return args_
            except:
                None
    # =============================================================
    # parametros{especificar a mensagem, nome do contato}

    def send(self, contato, mensagem):

        # time de espera de -> 0 seg
        time.sleep(0)
        # verifica se a barra de pesquisa existe
        # se sim ele retorna a barra de pesquisa
        object = self.findElement_Select(
            args='div[title="Caixa de texto de pesquisa"]')
        # clica no elemento selecionado
        object.click()
        # escreve o contato na barra
        object.send_keys(f'{contato}')
        # time de espera de -> 2 seg
        time.sleep(2)
        # seleciona o elemento -> span ('nome do contato')
        object = self.findElement_Select(args=f'span[title="{contato}"]')
        # clica no elemento selecionado
        object.click()
        # seleciona o elemento -> div Mensagem
        object = self.findElement_Select(args='div[title="Mensagem"]')
        # envia a mensagem para o elemento selecionado
        object.send_keys(f'{mensagem}')
        # seleciona o elemento -> SEND
        object = self.findElement_Select(args='span[data-icon="send"]')
        # clica no elemento selecionado
        object.click()
        # time de espera de -> 2 seg
        time.sleep(2)

    def read(self, contato):
        driver = self.driver
        pesquisar = self.IsLoadSearch()
        pesquisar.click()
        pesquisar.send_keys(f'{contato}')
        time.sleep(2)
        while True:
            try:
                contato_ = driver.find_element(
                    By.CSS_SELECTOR, f'span[title="{contato}"]')
                break
            except:
                pass
        contato_.click()
        time.sleep(5)
        read_msg = driver.find_elements(By.CSS_SELECTOR, 'div[role="row"]')
        for linha in read_msg:
            lista_msg.append(linha.text)
        return lista_msg
