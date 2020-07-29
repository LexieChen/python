#!/usr/bin/python3

import socket
import sys

HOST = 'localhost'
PORT = 50051
CHUNKSIZE = 1024
HDR_LENGTH = 200


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

while True:
    conn, addr = server.accept()
    isFirst = True
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(CHUNKSIZE)
            if isFirst:
                isFirst = False
                flen = int(data[:HDR_LENGTH])
                fname = data[HDR_LENGTH:HDR_LENGTH+flen]
                print(f'fname is {fname}')
                fo = open(fname, 'wb')
                fo.write(data[HDR_LENGTH+flen:])
            else:
                if not data:
                    fo.close()
                    break
                fo.write(data)

#except:
#    print('Get error: ', sys.exc_info()[0])
#    sys.exit(1)
