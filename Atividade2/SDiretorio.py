from const import *
import rpyc
from rpyc.utils.server import ThreadedServer


class SDiretorio(rpyc.Service):
    
    serverNEncontrado = f"Server não encontrado ou não existente"
    
    ListaDiretorio = {}
    
    def __init__(self, lista):
        self.ListaDiretorio = lista

    def exposed_registraServer(self, serverName, ipAdress, portNum):
        self.ListaDiretorio.update({serverName : (ipAdress, portNum)})
        print(f"Registrando Server")
        print(self.ListaDiretorio)

    def exposed_buscaServer(self, serverName):
        print(f"Buscando Server")
        print({serverName})
        print(f"tem no dic: {serverName in self.ListaDiretorio}")

        if  serverName in self.ListaDiretorio:
            print(f"Server encontrado")
            print(self.ListaDiretorio)
            return self.ListaDiretorio[serverName]
        else:
            print(f"Server não encontrado")
            print(self.ListaDiretorio)
            return self.serverNEncontrado


if __name__ == "__main__":
    ListaDiretorio = {}
    print(f"Iniciando servidor de diretórios na porta: {PORTDIR}")
    SDiretorio = ThreadedServer(SDiretorio(ListaDir), port=12307)
    SDiretorio.start()
