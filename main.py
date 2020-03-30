#!/usr/bin/python env
import clipboard as c

def readTxt(source):
    with open(source, 'r') as s:
        s = s.read()
        return s


def clipboard(source):
    c.copy(source)

    #t = c.paste()
    #print(t)
#readTxt('clipboard.txt')


if __name__ == '__main__':
    clipboard(readTxt('clipboard.txt'))