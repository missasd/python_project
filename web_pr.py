#coding:utf-8
import socket
s = socket.socket()
# 生成socket模块的socket类的一个实例

host = socket.gethostname()
port = 1234
s.bind((host, port))  # 将套接字bind到host，port组成的元组上

s.listen(5) # listen方法监听特定的端口
while True:
    c.send

