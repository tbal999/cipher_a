# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 18:11:11 2019

@author: thoma
"""
import os
def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

#cipher input.
cipher1_input = input("Type in cipher1 here:" )
cipher2_input = input("Type in cipher2 here:" )
cipher3_input = input("Type in cipher3 here:" )
cipher = (int(cipher1_input),int(cipher2_input),int(cipher3_input))

string_input = input("Type in string here:" )
stringlist = []
for i in string_input:
    stringlist.append(ord(i))

def encode():
    xindex = 0
    yindex = 0
    for i in stringlist[xindex:]:
        for a in cipher[yindex:]:
            print(a,i)
            stringlist[xindex] = stringlist[xindex] + a
            yindex = yindex + xindex
        xindex = xindex+1
        yindex = 0
        
def decode():
    xindex = 0
    yindex = 0
    for i in stringlist[xindex:]:
        for a in cipher[yindex:]:
            print(a,i)
            stringlist[xindex] = stringlist[xindex] - a
            yindex = yindex - xindex
        xindex = xindex+1
        yindex = 0
    
def printX():
    chrlist = []
    for i in stringlist:
        chrlist.append(chr(i))
    seperator = ''
    printy = seperator.join(chrlist)
    print(printy)
    addToClipBoard(printy)
    chrlist.clear()
    start()
    
def quitoK():
    quit()
    
def start():
    print(cipher)
    print(stringlist)
    x = input("Type encode, decode, print (or quit):" )
    if x == "encode":
        encode()
    if x == "decode":
        decode()
    if x == "print":
        printX()
    if x == "quit":
        quitoK()
    else:
        start()
    
start()
