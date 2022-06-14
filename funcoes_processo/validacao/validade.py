from os import stat


def forms(msg_cliente='',dic=[],status= False):
    for x in range(len(dic)):
        if msg_cliente == dic[x]:
            return status
   
    dados=False
    return dados