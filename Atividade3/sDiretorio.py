from const import *
import rpyc
from rpyc.utils.server import ThreadedServer


class SDiretorio(rpyc.Service):
    
    sInexistente = f"Server não encontrado ou não existente"
    sNaoRegistrado = f"Servidor nao registrado"
    ListaDiretorio = {}
    
    def __init__(self, lista):
        self.ListaDiretorio = lista

    def exposed_registraServer(self, serverName, ipAdress, portNum):
        self.ListaDiretorio.update({serverName : (ipAdress, portNum)})
        print(f"Registrando Server")
        print(self.ListaDiretorio)

    def exposed_buscaServer(self, serverName):
        print(f"Buscando Server")

        if  serverName in self.ListaDiretorio:
            print(f"Server encontrado")
            return self.ListaDiretorio[serverName]
        else:
            print(f"Server não encontrado")
            return self.sInexistente

    def exposed_registraServerNovamente(self, serverName, ipAdress, portNum):
        print(f"Registrando Server Novamente")
        if serverName in self.ListaDiretorio:
            print(f"Achou item que vai ser registrado novamente")
            self.ListaDiretorio[serverName] = (ipAdress, portNum)
            return self.ListaDiretorio[serverName]
        else:
            print(f"Item nao registrado")
            return self.sNaoRegistrado

    def exposed_removaServer(self, serverName):
        print(f"Removendo Server")
        if  serverName in self.ListaDiretorio:
            print(f"Achamos o server a ser removido")
            ElementoRemovido = self.ListaDiretorio[serverName]
            print(f"Guardando o elemento: {ElementoRemovido} para ser usado no return")
            self.ListaDiretorio.pop(key=serverName)
            print(f"Removendo elemento do servidor")
            return ElementoRemovido
        else:
            print(f"Nao achamos o server a ser removido")
            return self.sNaoRegistrado

if __name__ == "__main__":
    ListaDiretorio = {}
    print(f"Iniciando servidor de diretórios na porta: {PORTDIR}")
    SDiretorio = ThreadedServer(SDiretorio(ListaDiretorio), port=12307)
    SDiretorio.start()
