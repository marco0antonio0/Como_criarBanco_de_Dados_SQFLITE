import PySimpleGUI as sg
from bot import whats
def upstatus(msg='',msgf=''):
    if len(msgf)>0:
        msgf =msgf +' '+ msg+'\n'
    else:
        msgf = msg
    print(msgf)
    return msgf
bot = whats()
bot.abrirWhatsapp() 
inicio = True
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Bot-whats')],
            [sg.Text('Contato'),sg.Input(key='contato')],
            [sg.Text('Mensagem'),sg.Input(key='mensagem')],
            [sg.Text(key='status')],
            [sg.Button('Enviar')]]
          

# Create the Window
window = sg.Window('Bot Whatsapp', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Enviar' and len(values['contato']) > 0 :
        msg = upstatus(msg='iniciado')
        window['status'].update(msg)            
        mensagens = bot.send(contato=values['contato'],mensagem=values['mensagem'])
        msg = upstatus(msg='mensagem sendo enviada',msgf=msg)
        window['status'].update(msg)
        bot.atualizar()
        msg = upstatus(msg='mensagem enviada com sucesso ',msgf=msg)
        window['status'].update(msg)
        inicio = False
    

window.close()