#!/usr/bin/python3

import random
import time

i = 0

fo = open('medium_file.txt', 'wb')

while(i < 1000):
    seq = range(256)
    s = random.choice(seq)
    fo.write(bytes(chr(s), encoding='utf8'))
    ++i
    if (i % 1000):
        time.sleep(1)


fo.close()
