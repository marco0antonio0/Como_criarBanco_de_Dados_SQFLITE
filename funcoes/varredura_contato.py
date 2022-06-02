import time
#==============================================================
#              Bloco verifica se ja carregou a pagina
#==============================================================     
def status_carregamento(driver):
    status_de_carregamento = True
    while status_de_carregamento:
      try:
        status = driver.find_element_by_xpath('//*[@id="pane-side"]')
        status_de_carregamento = False
        time.sleep(1)
        return status
      except:
        None

def varreduras_de_contatos(driver):
    status_carregamento(driver=driver)
    i = 11
    for x in range(12):
      if x!=0:
        try:
          selecionar = driver.find_element_by_xpath('//*[@id="pane-side"]/div/div/div/div[{}]/div/div/div[2]/div[1]/div[1]/span'.format(i)).text
          print('{} - '.format(x)+selecionar)          
        except:
          None
      i-=1