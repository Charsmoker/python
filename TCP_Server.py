import socket,threading,time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##监听端口，这个ip地址可以绑定到所有的网络地址
s.bind(('0.0.0.0', 9999))
##开始监听，里面的参数指定等待连接的最大数量
s.listen(5)
print('Waiting for connection...')

def tcplink(sock, addr):
    print(f'Accept new connection from {addr}:{addr}')
    sock.send(b'welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send((f'Fuck You, %s!' %data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print(f'Connection from {addr}:{addr} closed.')

while True:
    ##接受一个新连接
    sock, addr = s.accept()
    ##创建一个新线程来处理TCP连接
    t = threading.Thread(target = tcplink , args = (sock, addr))
    t.start()

