import time
# ==============================================================
#               Varredura ao iniciar para
#               procurar se tem box seach
# ==============================================================

def existe_box(driver):
    while True:
        try:
            click_box_mensage = driver.find_element_by_class_name('p3_M1')
            return click_box_mensage
        except:
            None

# ==============================================================
#               Varredura ao iniciar para
#               procurar se tem box seach
# ==============================================================


def varredura(driver):
    while True:
        try:
            pesquisar = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
            return pesquisar
        except:
            None
    # ==============================================================


def enviarMensagem(driver, contato, mensagem, opcao):
    # ==================================================================================
    #           def enviarMensagem(driver,contato,mensagem,opcao)
    # ==================================================================================
    if opcao == 1:

        #
        # ==============================================================
        #         parte 2
        # ==============================================================
        #              encontrado o boxSeach
        # ==============================================================
        pesquisar = varredura(driver)

        # ==============================================================
        #         parte 2.1
        # ==============================================================
        #              irar clicar boxSeach
        # ==============================================================
        time.sleep(3)
        pesquisar.click()

        # ==============================================================
        #         parte 3
        # ==============================================================
        #              Ira escrever algo no boxSeach
        # ==============================================================
        pesquisar.send_keys(contato)
        # ==============================================================
        # ==============================================================
        #         parte 4
        # ==============================================================
        #              Irar selecionar o contato desejado
        #               e irar clicar
        # ==============================================================
        time.sleep(4)
        while True:
            try:
                procurar_contato = driver.find_element_by_xpath("//span[@title='{}']".format(contato))
                procurar_contato.click()
                print('to aqui')
                break
            except:
                None
        # ==============================================================
        #                       parte 5
        # ==============================================================
        #              Irar selecionar o boxMensagem --
        #           Irar escrever a mensagem desejada --
        #            Irar clicar em enviar mensagem --
        # ==============================================================
        time.sleep(3)
        click_box_mensage = existe_box(driver=driver)
        click_box_mensage.click()
        time.sleep(2)
        click_box_mensage.send_keys(mensagem)
        time.sleep(3)
        # ==============================================================
        #         parte 7                              --
        # ==============================================================
        #          Irar clicar em enviar mensagem
        # ==============================================================
        time.sleep(2)

        while True:
            try:
                
                btn_envia_mensagem = driver.find_element_by_xpath('//span[@data-icon="send"]')
                if btn_envia_mensagem != None:
                    btn_envia_mensagem = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
                    btn_envia_mensagem.click()
                    print('procurando btn')
                    break
                break
            except:
                None

    # ==================================================================================
    #               def enviar_msg_processo(driver,mensagem):
    # ==================================================================================
    if opcao == 2:
        # ==============================================================
        #         parte 5
        # ==============================================================
        #              Irar selecionar o boxMensagem --
        # ==============================================================
        click_box_mensage = existe_box(driver=driver)
        click_box_mensage.click()

        # ==============================================================
        #         parte 6
        # ==============================================================
        #           Irar escrever a mensagem desejada --
        # ==============================================================
        click_box_mensage.send_keys(mensagem)

        # ==============================================================
        #         parte 7                              --
        # ==============================================================
        #          Irar clicar em enviar mensagem
        # ==============================================================
        while True:
            try:
                btn_envia_mensagem = driver.find_element_by_xpath('//span[@data-icon="send"]')
                print('to aqui')
                if btn_envia_mensagem != None:
                    btn_envia_mensagem = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
                    btn_envia_mensagem.click()
                    print('to aqui')

                break
            except:
                None
