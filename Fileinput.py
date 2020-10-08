#Write a Python program to read an entire text file.
def file_read(fname):
        txt = open(fname)
        print(txt.read())

file_read('test.txt')

#Write a Python program to read first n lines of a file. 
def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('test.txt',2)
