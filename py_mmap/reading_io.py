#!/usr/bin/python3 

import sys
import timeit
import mmap
import re

def regular_io(filename):
    with open(filename, mode="r", encoding="utf-8") as file_obj:
        text = file_obj.read();
        #print(text)

def mmap_io(filename):
    with open(filename, mode="r", encoding="utf-8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_file:
            text = mmap_file.read()
            #print(text)

def regular_find(filename):
    with open(filename, mode='r', encoding='utf-8') as file_obj:
        text = file_obj.read()
        text.find(" integer ")

def mmap_find(filename):
    with open(filename, mode='r', encoding='utf-8') as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_file:
            mmap_file.find(b" integer ")

def regular_exp(filename):
    exp = re.compile(r"\b[a-zA-Z]{5}\b")
    with open(filename, mode='r', encoding='utf-8') as file_obj:
        text = file_obj.read()
        exp.findall(text)

def mmap_exp(filename):
    exp = re.compile(rb"\b[a-zA-Z]{5}\b")
    with open(filename, mode='r', encoding='utf-8') as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_file:
            words = exp.findall(mmap_file)



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

    print("regular find\n",
    timeit.repeat("regular_find(f)",
        repeat=3,
        number=1,
        setup="from __main__ import regular_find, f")
    )

    print("mmap find\n",
    timeit.repeat("mmap_find(f)",
        repeat=3,
        number=1,
        setup="from __main__ import mmap_find, f")
    )

    print("regular exp\n",
    timeit.repeat("regular_exp(f)",
        repeat=3,
        number=1,
        setup="from __main__ import regular_exp, f")
    )

    print("mmap exp\n",
    timeit.repeat("mmap_exp(f)",
        repeat=3,
        number=1,
        setup="from __main__ import mmap_exp, f")
    )
