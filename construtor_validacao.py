class validar_resposta:
  def __init__(self,msg_cliente) :
    self.msg = msg_cliente

  def opcao_x(self,opcao):
    #==============================================
    # opção 1
    # opcao[ id_opcao ][ mensagem_resposta, passou ]
    for i in opcao[0][2]:
      if i == self.msg:
        mensagem = opcao[0][0]
        dados =[mensagem,opcao[0][1]]
        return dados
    #==============================================
    # opção 2
    # opcao[ id_opcao, passou, mensagem_resposta]
    for i in opcao[1][2]:
      if i == self.msg:
        mensagem = opcao[1][0]
        dados =[mensagem,opcao[1][1]]
        return dados
    #==============================================
    # opção errada
    # opcao[ id_opcao, passou, mensagem_resposta]
    mensagem = opcao[2][0]
    dados =[mensagem,False]
    return dados
    
def realizar_pergunta(opcao,msg_cliente):
  #==============================================================================
  perguntar= validar_resposta(msg_cliente=msg_cliente).opcao_x(opcao=opcao)
  return perguntar
  #==============================================================================