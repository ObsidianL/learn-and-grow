# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:29:16 2019

@author: An
"""

import socket
#导入套接字模块

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# - socket.AF_INET：IPV4
# - socket.STREAM：TCP
# - socket.DGRAM：UDP

s.bind(('',25555))
#绑定套接字有效地址和端口
#''空位任何地址 本地的127.0.0.1 和局域网还有自己真实的ip
print('[+] Server Open.....')

while True:
    try:
        data,c_addr = s.recvfrom(1024)
        #一次性接受1024bytes的数据 ，返回一个元组，其中有数据和地址
        #UDP不需要构成连接，直接发送即可
        mess = "已经收到请继续"
        #data = data+ mess
        print('from:',c_addr)
        #c_addr是一个地址,发送消息的客户端的IP和端口的二元组
        print('say：%s'%(data.decode('utf-8')))
        s.sendto(mess.encode('utf-8'),c_addr)
        msg = data.decode('utf-8')
        s.sendto(msg.encode('utf-8'),c_addr)
        #发送信息，其中有两个参数，一个是信息，一个是目标地址和端口
        
    except KeyboardInterrupt:
        break

print('[+] Server Close......')
s.close
