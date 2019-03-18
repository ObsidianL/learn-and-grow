# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:20:24 2019

@author: An
"""
import socket
#导入套接字模块

c = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# - socket.AF_INET：IPV4
# - socket.STREAM：TCP
# - socket.DGRAM：UDP

while True:
    try:
        msg = input('>>>')
        if msg == 0:
            #判断输入是否为空 就是直接回车了
            continue
        #UDP不需要构成连接，直接发送即可
        c.sendto(msg.encode('utf-8'),('127.0.0.1',25555))
        #发送消息，其中两个参数,第一个是要发送的信息
        #第二个是发送的ip地址和端口，是一个元组

        data,s_addr = c.recvfrom(1024)

        #c_addr是一个地址,发送消息的客户端的IP和端口的二元组
        print('$: %s'%(data.decode('utf-8')))
    except KeyboardInterrupt:
        break

c.close()

