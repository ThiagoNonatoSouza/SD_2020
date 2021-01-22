import rpyc
from const import *

class Client:
  print(f"Iniciando conexão com servidor de diretórios de  ip: {SDIRETORIO} e porta: {PORTDIR}")
  
  conn = rpyc.connect(SDIRETORIO, PORTDIR) # Connect to the server
  
  print(f"Fazendo busca de Fibra")
  
  nomeDir  =  conn.root.exposed_buscaServer('Fibra')
  
  print(f"Busca finalizada, resultado: ")
  print(nomeDir) # Print the result
