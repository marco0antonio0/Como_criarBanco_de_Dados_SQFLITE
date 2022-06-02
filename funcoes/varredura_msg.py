import time
t = True
# ==============================================================
#               Varredura ao iniciar para
#               procurar se tem box seach
# ==============================================================


def varredura(driver):
    status_de_varredura = True
    while status_de_varredura:
        try:
            #                                         //*[@id="side"]/div[1]/div/div/div[2]/div/div[2]
            pesquisar = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
            status_de_varredura = False
            return pesquisar
        except:
            None
# ==============================================================


def varredura_msg(driver, contato):
    # ==============================================================
    #         parte 2
    # ==============================================================
    #              encontrado o boxSeach

    # ==============================================================
    #pesquisar = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    pesquisar = varredura(driver)
    try:
        procurar_contato = driver.find_element_by_xpath("//span[@title='{}']".format(contato))
        procurar_contato.click()

    except:
        None

    if procurar_contato != None:
        # ==============================================================
        #  varrer os dados e ver se tem mensagem , se tiver ele retorna
        i = 12
        for x in range(12):
            if x != 0:
                try:
                    #selecionar_msg = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[3]/div[37]/div/div[1]/div[1]/div[1]/div/span[1]/span'.format(i)).text
                    # i0jNr
                    selecionar_msg = driver.find_elements_by_xpath("//span[@class='i0jNr selectable-text copyable-text']")
                except:
                    None
                i -= 1

        return selecionar_msg

    else:
        # ==============================================================
        #         parte 2.1
        #              irar clicar boxSeach
        # ==============================================================
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
        # ==============================================================
        while t:
            try:
                procurar_contato = driver.find_element_by_xpath("//span[@title='{}']".format(contato))
                procurar_contato.click()
                break
            except:
                None

        # ==============================================================

        # ==============================================================
        #  varrer os dados e ver se tem mensagem , se tiver ele retorna
        i = 12
        for x in range(12):
            if x != 0:
                try:
                    #selecionar_msg = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[3]/div[37]/div/div[1]/div[1]/div[1]/div/span[1]/span'.format(i)).text
                    # i0jNr
                    selecionar_msg = driver.find_elements_by_xpath("//span[@class='i0jNr selectable-text copyable-text']")
                except:
                    None
                i -= 1
        return selecionar_msg
