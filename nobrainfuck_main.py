#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Nicolas V custom edition):
# Nicolas V wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. But please say it's me that did it,
# because I seek for eternal glory. If we meet some day, and you think
# this stuff is funny, you can buy me a beer in return.
# ----------------------------------------------------------------------------
#
from optparse import OptionParser
from sys import stdout,stdin,argv
import nbfparser
import random

_VOWELS = set(["i","a","o","u","e","y"])

def bf_to_nbf(content):
    lst = []
    def echo(st):
        st = st.capitalize()
        sta = []
        for i in st:
            if i in _VOWELS:
                prob = random.randint(0,9)
                if prob == 0:
                    sta.append(i + i + i)
                elif prob <= 4:
                    sta.append(i + i)
                else:
                    sta.append(i)
            else:
                sta.append(i)
        st = "".join(sta)
        lst.append(st) 

    for i in content:
        if i == ">":
            echo("ho")
        elif i == "<":
            echo("ha")
        elif i == "+":
            echo("yes")
        elif i == "-":
            echo("no")
        elif i == ".":
            echo("my god")
        elif i == ",":
            echo("harder")
        elif i == "[":
            echo("not yet")
        elif i == "]":
            echo("i'm comming")
    return " ".join(lst)

# Tiny Brainfuck Interpreter; Author: Alex McNeil, 30 March 2010; License: GPLv2
def interpret_bf(code):
    cells = {0:0}
    cPtr = ptr = 0
    while cPtr < len(code):
        matching = 0
        c = code[cPtr]
        if c == ">":
            ptr += 1
            if not ptr in cells: cells[ptr] = 0
        elif c == "<":
            ptr -= 1
            if not ptr in cells: cells[ptr] = 0
        elif c == "+": cells[ptr] = cells[ptr] + 1
        elif c == "-": cells[ptr] = cells[ptr] - 1
        elif c == ".": stdout.write(chr(cells[ptr]))
        elif c == ",": cells[ptr] = ord(stdin.read(1))
        elif c == "[" and cells[ptr] == 0:
            for x in xrange(cPtr,len(code)):
                if code[x] == '[': matching += 1
                elif code[x] == ']':
                    if matching > 0: matching -= 1
                    if matching == 0: cPtr = x; break
        elif c == "]" and cells[ptr] != 0:
            for x in xrange(cPtr,-1,-1):
                if code[x] == ']': matching += 1
                elif code[x] == '[':
                    if matching > 0: matching -= 1
                    if matching == 0: cPtr = x; break
        cPtr += 1
# end of Alex McNeil code

def main():
    parser = OptionParser(usage="usage: %prog [options] filename")
    parser.add_option("-b", "--bf-to-nbf",
                      action="store_true", dest="to_nbf", default=False,
                      help="Convert Brainfuck to Nobrainfuck")

    (options, args) = parser.parse_args()

    if len(args) < 1:
        parser.print_help()
        exit(-1)
    with open(args[0]) as f:
        content = f.read()

    if options.to_nbf: 
        trad = bf_to_nbf(content)
        print trad
    else:
        trad = nbfparser.parse("program", content)
        interpret_bf(trad)


if __name__ == "__main__":
    main()

