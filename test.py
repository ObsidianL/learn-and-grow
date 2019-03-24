from socket import *
import threading
serverPort = 8081
serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('',serverPort))  #将套接字绑定到地址。address地址的格式取决于地址族。在AF_INET下，以元组（host,port）的形式表示地址。
serverSocket.listen(5)  #开始监听传入连接。backlog指定在拒绝连接之前，可以挂起的最大连接数量。
                        #backlog等于5，表示内核已经接到了连接请求，但服务器还没有调用accept进行处理的连接个数最大为5
print("Server is ready to work")


def deal(conn,addr):
    sendflie = open("1.txt", "rb")
    sentence = conn.recv(1024)
    print(sentence.decode())
    while(True):
         #　接受套接字的数据。数据以字符串形式返回，bufsize指定最多可以接收的数量。flag提供有关消息的其他信息，通常可以忽略。
        info = sendflie.read(1024)
        if(info):
            conn.send(info)
        else:
            break
    sendflie.close()




while(True):
    (conn,addr) = serverSocket.accept()#接受连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
    server = threading.Thread(target= deal,args =(conn,addr))
    server.start()

#serverSocket.close()






from socket import *
import threading
import os
flag = 0


def request(clientSocket):
    while(True):
        reqt = input()
        if(len(reqt) == 0):
            continue
        elif(reqt == "exit"):
            global flag
            flag = 1
            os._exit(0)
        else:
            clientSocket.send(reqt.encode())
        #clientSocket.send(reqt.encode())


def recv(clientSocket):
    newile = open("new1.txt","wb")
    while(True):
        reps = clientSocket.recv(1024)
        if(reps):
            newile.write(reps)
            print(reps.decode())

        else:
            newile.close()
            break
        print("have recieved")
        #print("From server:",reps.decode())

def control(clientSocket):
    global flag
    if(flag):
            clientSocket.close()
            os._exit(0)


serverName = '172.26.94.147'
serverPort = 8081
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

req = threading.Thread(target = request,args = (clientSocket,))#send the data and request to thes server
req.start()

monitor = threading.Thread(target = recv,args = (clientSocket,))#listen to the server's response,and deal withe it
monitor.start()

control = threading.Thread(target= control,args = (clientSocket,))#control the program,close the conection and exit
control.start()

