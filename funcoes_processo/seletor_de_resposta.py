from funcoes_processo.fn_processamento import processamento


def passarEtapa(nome,etapa):
  etapasContatos.pop()
  etapasContatos.append([nome,etapa])
  status_ = False
  print(etapasContatos)
  return status_
# etapasContatos[id][nome,etapa]
# etapasContatos[id][ 0,  1 ]

etapasContatos = []
def seletor_de_eventos(nome_contato,lista_mensagens):
  status = True
  #============================================
  #         Varrer Lista
  for i in range(0,len(etapasContatos)): 
    #==========================================
    #       Procurar nome na lsita 
    if nome_contato == etapasContatos[i][0]:
      #========================================
      #     Etapa 1
      if 1 == etapasContatos[i][1]:
        etapa = etapasContatos[i][1]+1
        nome = etapasContatos[i][0]
        status =passarEtapa(nome=nome,etapa=etapa)
        return processamento(etapa=0)
      #========================================
      #     Etapa 2
      if 2 == etapasContatos[i][1]:
        etapa = etapasContatos[i][1]+1
        nome = etapasContatos[i][0]
        status =passarEtapa(nome=nome,etapa=etapa)
        return processamento(etapa=etapa)
      #========================================
      #     Etapa 3
      if 3 == etapasContatos[i][1]:
        etapa = etapasContatos[i][1]+1
        nome = etapasContatos[i][0]
        status =passarEtapa(nome=nome,etapa=etapa)
        return processamento(etapa=5)
      if  3<etapasContatos[i][1]:
        status = False
        print('etapas d++')
        break

  if status:
    nome = nome_contato
    etapa = 0
    etapasContatos.append([nome,etapa])
    print(etapasContatos)
    return processamento(etapa=0)
  