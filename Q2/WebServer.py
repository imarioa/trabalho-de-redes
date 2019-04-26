#import socket module
from socket import *
import sys
import os

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepara o socket servidor
serverSocket.bind(('', 8080))
serverSocket.listen(1)
while True:
	#Estabelece a conexão
    print ('Ready to serve...')
    
    connectionSocket, addr = serverSocket.accept()
    try:
        #codigo_inicio
        message = connectionSocket.recv(1024)
        #codigo_fim
        
        filename = message.decode().split()[1]

        #abrindo arquivo solicitado pelo cliente
        f = open(os.getcwd() + filename, 'r')

        #codigo_inicio
        outputdata = f.readlines()
        #codigo_fim

        #Envia um linha de cabeçalho HTTP para o socket
        #codigo_inicio
        connectionSocket.send('HTTP/1.0 200 OK\n'.encode())
        #codigo_fim

        #Envia o conteúdo do arquivo solicitado ao cliente
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
        
    except IOError:
    	#Envia uma mensagem de resposta "File not found"
        error = 'File not found'
       # connectionSocket.send('HTTP/1.0 404 NOT_FOUND\n'.encode())
        connectionSocket.send(error.encode())
        connectionSocket.close()
serverSocket.close() 
sys.exit()#Termina o programa depois de enviar os dados


