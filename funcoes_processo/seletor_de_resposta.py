# etapasContatos[id][nome,etapa]
# etapasContatos[id][ 0,  1 ]
status = True
etapasContatos = []
def seletor_de_eventos(nome_contato,lista_mensagens):
  #============================================
  #         Varrer Lista
  for i in range(0,len(etapasContatos)): 
    #==========================================
    #       Procurar nome na lsita 
    if nome_contato == etapasContatos[i][0]:
      #========================================
      #     Etapa 1
      if 1 == etapasContatos[i][1]:
        etapa = etapasContatos[i][1]
        nome = etapasContatos[i][0]
        print('etapa ',etapa)
        #status = False
        break
      #========================================
      #     Etapa 2
      if 2 == etapasContatos[i][1]:
        etapa = etapasContatos[i][1]
        nome = etapasContatos[i][0]
        print('etapa ',etapa)
        #status = False
        break
      #========================================
      #     Etapa 3
      if 3 == etapasContatos[i][1]:
        etapa = etapasContatos[i][1]
        nome = etapasContatos[i][0]
        print('etapa ',etapa)
        #status = False
        break
  if status:
    nome = nome_contato
    etapa = 1
    etapasContatos.append([nome,etapa])
    print('etapa ',etapa)
    print(etapasContatos)
  