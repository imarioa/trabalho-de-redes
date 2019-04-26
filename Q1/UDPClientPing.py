import time
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)

# To set waiting time of one second for reponse from server
clientSocket.settimeout(1)

# Declare server's socket address
remoteAddr =(('127.0.0.1', 12000))

# Ping ten times
for i in range(10):
    
    tempoEnvio = time.time()
    message = 'Ping ' + str(i + 1) + " " + str(time.strftime("%H:%M:%S"))
    clientSocket.sendto(message.encode(), remoteAddr)
    
    try:
        mensagem, server = clientSocket.recvfrom(1024)
        tempoRec = time.time()
        rtt = tempoRec - tempoEnvio
        round(rtt,2)
        print (mensagem)
        print ('RTT', round(rtt,4),'s','\n')
        print 
    
    except timeout:
        print ('Solicitação expirada\n')
        print