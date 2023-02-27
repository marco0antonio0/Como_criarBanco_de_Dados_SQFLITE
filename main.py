from bot import Bot
mensagem = """*Bot whatsapp* - Capivara  
 Estou testando"""
contato = 'Marco Antonio'
instance = Bot()
instance.abrirWhatsapp()
instance.send(contato=contato, mensagem=mensagem)
