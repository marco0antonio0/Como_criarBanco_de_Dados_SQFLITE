import time
#==============================================================
#               Varredura ao iniciar para
#               procurar se tem box seach
#==============================================================     
t= True 
def existe_box(driver):
   while t:
    try:
      click_box_mensage = driver.find_element_by_class_name('p3_M1')
      return click_box_mensage
    except:
      None

y= True 
#==============================================================
#               Varredura ao iniciar para
#               procurar se tem box seach
#==============================================================     
def varredura(driver):
  status_de_varredura = True
  while status_de_varredura:
    try:
      pesquisar = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
      return pesquisar
    except:
      None
  #==============================================================  
def enviarMensagem(driver,contato,mensagem,opcao):
  #==================================================================================
  #           def enviarMensagem(driver,contato,mensagem,opcao)
  #==================================================================================
  if opcao == 1:
    time.sleep(2)
    #
    #==============================================================
    #         parte 2
    #==============================================================
    #              encontrado o boxSeach
    #==============================================================
    pesquisar = varredura(driver)

    #==============================================================
    #         parte 2.1
    #==============================================================
    #              irar clicar boxSeach
    #==============================================================
    pesquisar.click()
    #==============================================================
    #         parte 3 
    #==============================================================
    #              Ira escrever algo no boxSeach
    #==============================================================
    pesquisar.send_keys(contato)
    #==============================================================
    #==============================================================
    #         parte 4
    #==============================================================
    #              Irar selecionar o contato desejado
    #               e irar clicar
    #==============================================================
    time.sleep(2)
    v = True
    while v:
      try:
        procurar_contato = driver.find_element_by_xpath("//span[@title='{}']".format(contato))
        procurar_contato.click()
        break
      except:
        None
    #==============================================================
    #         parte 5
    #==============================================================
    #              Irar selecionar o boxMensagem --
    #           Irar escrever a mensagem desejada --
    #============================================================== 
    time.sleep(2)
    v = True
    while v:
      try:
        click_box_mensage = driver.find_element_by_class_name('p3_M1')
        click_box_mensage.click()
        click_box_mensage.send_keys(mensagem)
        break
      except:
        None
    #==============================================================
    #         parte 7                              --
    #==============================================================
    #          Irar clicar em enviar mensagem
    #==============================================================
    time.sleep(2)
    v = True
    while v:
      try:
        btn_envia_mensagem = driver.find_element_by_xpath('//span[@data-icon="send"]')
        if btn_envia_mensagem !=None:
          btn_envia_mensagem = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
          btn_envia_mensagem.click()
        
        break
      except:
        None


    time.sleep(3)

    
  #==================================================================================
  #               def enviar_msg_processo(driver,mensagem):
  #==================================================================================
  if opcao == 2:
    #==============================================================
    #         parte 5
    #==============================================================
    #              Irar selecionar o boxMensagem --
    #==============================================================  
    click_box_mensage = existe_box(driver=driver)
    click_box_mensage.click()
    time.sleep(2)

    #==============================================================
    #         parte 6
    #==============================================================
    #           Irar escrever a mensagem desejada --
    #==============================================================
    click_box_mensage.send_keys(mensagem)
    time.sleep(2)
    #==============================================================
    #         parte 7                              --
    #==============================================================
    #          Irar clicar em enviar mensagem
    #==============================================================
    time.sleep(2)
    v = True
    while v:
      try:
        btn_envia_mensagem = driver.find_element_by_xpath('//span[@data-icon="send"]')
        if btn_envia_mensagem !=None:
          btn_envia_mensagem = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
          btn_envia_mensagem.click()
        
        break
      except:
        None
    time.sleep(3)

    



