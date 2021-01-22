import rpyc
import socket
from const import * #-
from rpyc.utils.server import ThreadedServer
 
class Fibra(rpyc.Service):
  value = []

  def exposed_append(self, data):
    
    print(f"Concatenando valor: {data}")
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    print(f"Retornando valor")
    return self.value

if __name__ == "__main__":
  print(f"Criando server Fibra") 
  server = ThreadedServer(Fibra, port = PORT)
  print(f"Conectando ao Server de diretório")  
  conn_serverDir = rpyc.connect(SERVERDIRETORIO,PORTDIR)
  print(f"Obtendo ipadress da Fibra")  
  ipAdress = socket.gethostbyname(socket.gethostname())
  print(f"Registrando no Server de diretório") 
  conn_serverDir.root.exposed_registraServer('Fibra',ipAdress,PORT)
  server.start()

