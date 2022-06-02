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
#==============================================================


def varreduras_de_notificacao(driver):
  status_carregamento(driver=driver)
  i = 11
  lista_de_contatos = []
  for x in range(11):
    def varredura_bruta(i):
      v = True
      while v:
        try:
          selecionar_contact = driver.find_element_by_xpath('//*[@id="pane-side"]/div/div/div/div[{}]/div/div/div[2]/div[1]/div[1]/span'.format(i)).text
          selecionar_notify = driver.find_element_by_xpath('//*[@id="pane-side"]/div/div/div/div[{}]/div/div/div[2]/div[2]/div[2]/span[1]'.format(i)).text
        except:
          break
        if selecionar_notify !='':
          # lista_de_contatos[id,nome,qtd_notificação]
          lista_de_contatos.append([i,selecionar_contact,selecionar_notify])
          #lista_de_contatos.append(i)
          #lista_de_contatos.append(selecionar_contact)
          #lista_de_contatos.append(int(selecionar_notify))
          return lista_de_contatos          
        return lista_de_contatos
    
    dados=varredura_bruta(i)
    i-=1
  return dados    