#!/usr/bin/python3

import mmap
import sys

def mmap_io_write(filename):
    with open(filename, mode='r+') as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_WRITE) as mmap_file:
            mmap_file[10:16] = b"python"
            mmap_file.flush()
            print(mmap_file)


if __name__ == "__main__":
    f = sys.argv[1]
    mmap_io_write(f)
