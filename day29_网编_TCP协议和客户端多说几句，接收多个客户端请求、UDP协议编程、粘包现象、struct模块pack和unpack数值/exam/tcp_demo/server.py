import socket

sk = socket.socket()                # 实例化socket对象
sk.bind(('192.168.0.103', 9093))    # 申请操作系统资源
sk.listen()                         # 监听服务
print(sk)   # 服务端本身的 ip和端口

conn, addr = sk.accept()            # 三次握手
print(conn) # 包含服务端的ip、端口和 建立链接的客户端的ip和端口
print(addr) # 建立链接的客户端的ip和端口 ('192.168.0.103', 63124)

msg = conn.recv(1024).decode('utf-8') # 服务端接收和发送消息
print(msg)
send_msg = input('>>>').strip().encode('utf-8')
conn.send(send_msg)

conn.close()                        # 四次挥手

sk.close()                          # 关闭server端服务