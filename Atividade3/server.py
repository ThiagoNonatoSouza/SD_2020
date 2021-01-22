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
  
  def exposed_remove(self, data):
    if data in self.value:
      print(f"Removendo valor")
      self.value.remove(data)
      return self.value

  def exposed_search(self, data):
    if data in self.value:
      print(f"Retornando valor e posicao")
      return (data, self.value.index(data) + 1) 
           
if __name__ == "__main__":
  print(f"Criaando server Fibra") 
  server = ThreadedServer(Fibra, port = PORT)
  print(f"Conectando ao Server de diretório")  
  conn_serverDir = rpyc.connect(SDIRETORIO,PORTDIR)
  print(f"Obtendo ipadress da Fibra")  
  ipAdress = socket.gethostbyname(socket.gethostname())
  print(f"Registrando no Server de diretório") 
  conn_serverDir.root.exposed_registraServer('Fibra',ipAdress,PORT)
  server.start()

