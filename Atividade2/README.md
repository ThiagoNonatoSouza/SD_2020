##Tarefa de Programação 02: Descoberta automática do servidor de aplicação


#conts.py 
 O const.py é o arquivo em que é guardado o IP e a Porta do Servidor de Diretorio(SDiretorio).
 
#client.py
O client.py é o arquivo em que há o código de cliente que faz a conexão com servidor e faz requisição através do servidor de diretório(SDiretorio).

#server.py
o server.py é o arquivo no qual está o servidor(Fibra) que é o servidor que client.py busca.

#SDiretorio.py
o SDiretorio.py é um arquivo que recebe as funções de registrar o servidor, que recebe o nome do servidor, ip e porta e os registra. Além disso ele é quem faz as buscas dos servidores, o client.py passa o nome do servidor e então o servidor de diretório(SDiretorio) faz a busca nos registros.Ele faz um papel intermediário entre o server.py e o client.py.