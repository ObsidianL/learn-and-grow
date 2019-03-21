#server
from socket import *

serverPort = 8080
serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('',serverPort))
serverSocket.listen(2)
print("Server is ready to work")

while(True):
    (connectionSocket,addr) = serverSocket.accept()
    while(True):
        sentence = connectionSocket.recv(1024).decode()
        if(len(sentence) == 0):
            print("disable to connect")
            break;

        print("client:",sentence)        
        connectionSocket.send(sentence.encode())
serverSocket.close()



#client
from socket import *

serverName = '172.26.94.147'
serverPort = 8080

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))


while(True):
    sententce = input("please enter the command:")
    if(len(sententce) == 0):
        continue
    if(sententce =="exit"):
        break;
    clientSocket.send(sententce.encode())
    modifiedSentence = clientSocket.recv(1024)
    print("Frome server:",modifiedSentence.decode())
clientSocket.close()


