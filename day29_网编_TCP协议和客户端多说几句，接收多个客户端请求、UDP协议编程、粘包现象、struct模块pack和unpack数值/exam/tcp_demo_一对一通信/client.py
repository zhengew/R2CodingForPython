import socket

sk = socket.socket()                             # 实例化socket对象

sk.connect(('192.168.0.103', 9093))              # 请求与服务端进行链接 三次握手
print(sk)
send_msg = input('>>>').strip().encode('utf-8')  # 客户端发送和接收消息
sk.send(send_msg)
msg = sk.recv(1024).decode('utf-8')
print(msg)

sk.close()                                        # 客户端与服务端进行四次挥手