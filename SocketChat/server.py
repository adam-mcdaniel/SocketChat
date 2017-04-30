#!/usr/bin/python3
# coding: latin-1
import socket
try:
    clients = []
    def main():
        host = socket.gethostbyname(socket.gethostname())
        port = int(raw_input('Port:'))
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.bind((host,port))
        print('Server Started:\nHost: '+host+'\nPort:'+str(port))
        while True:
            data, addr = s.recvfrom(1024)
            print('conn recieved:' + str(addr))
            if addr not in clients:
                clients.append(addr)
            if data != '':
                data = data.decode('utf-8')
                data = str(data)
                print('from connected user:'+str(addr))
                print('sending:' +data)
                print(clients)
                data = str(data)
                if data == 'c':
                    sendto(str.encode('List of Clients:'+clients),addr)
                for x in clients:
                    if x != addr:
                        try:
                            s.sendto(str.encode('from user:'+str(addr)+':'+data),x)
                        except Exception as e:
                            print(e)
        s.close()
except Exception as e:
    print(e)
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
