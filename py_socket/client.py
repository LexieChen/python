#!/usr/bin/python3

import socket
import sys

HOST = 'localhost'
PORT = 50051
CHUNKSIZE = 1024
HDR_LENGTH = 200

msgList = ["hello, world 0", "hello, world 1", "hello world 2"]

if (len(sys.argv) < 3):
    print('Invalid input')
    sys.exit(1)

fname = sys.argv[1]
dest = sys.argv[2]
print(f'file is {fname}')

try:
    fo = open(fname, "rb")
except:
    print("Get error: ", sys.exc_info()[0])
    sys.exit(1)

#while True:
#    msg = fo.read(CHUNKSIZE)
#    if not msg:
#        break
#    print(msg)

destBin = dest.encode('ascii')
hdr = f'{len(destBin):<{HDR_LENGTH}}'
hdr = hdr.encode('ascii')

print(f'header {hdr}')
print(f'dest file name {dest}')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(hdr+destBin)
    while True:
        bstr = fo.read(CHUNKSIZE)
        if not bstr:
            fo.close()
            break
#        print(f'going to send {bstr}')
        s.send(bstr)
#        data = s.recv(1024)
#        print('Received', repr(data))
