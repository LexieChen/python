#!/usr/bin/python3 

import sys
import timeit
import mmap

def regular_io(filename):
    with open(filename, mode="r", encoding="utf-8") as file_obj:
        text = file_obj.read();
        #print(text)

def mmap_io(filename):
    with open(filename, mode="r", encoding="utf-8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_file:
            text = mmap_file.read()
            #print(text)

if __name__ == "__main__":
    f = sys.argv[1]
    print("regular read\n", 
    timeit.repeat("regular_io(f)",
            repeat=3,
            number=1,
            setup="from __main__ import regular_io, f")
    )

    print("mmap read\n", 
    timeit.repeat("mmap_io(f)",
            repeat=3,
            number=1,
            setup="from __main__ import mmap_io, f")
    )
