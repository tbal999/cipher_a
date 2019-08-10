# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 18:11:11 2019

@author: thoma
"""
codeindex = 0

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
    global codeindex
    xindex = 0
    yindex = 0
    for i in stringlist[xindex:]:
        for a in cipher[yindex:]:
            stringlist[xindex] = stringlist[xindex] + a
            yindex = yindex + xindex
        xindex = xindex+1
        yindex = 0
    codeindex = codeindex + 1
        
def decode():
    global codeindex
    xindex = 0
    yindex = 0
    for i in stringlist[xindex:]:
        for a in cipher[yindex:]:
            stringlist[xindex] = stringlist[xindex] - a
            yindex = yindex - xindex
        xindex = xindex+1
        yindex = 0
    codeindex = codeindex - 1
    
def printX():
    chrlist = []
    for i in stringlist:
        chrlist.append(chr(i))
    seperator = ''
    printy = seperator.join(chrlist)
    print(printy)
    chrlist.clear()
    start()
    
def quitoK():
    quit()
    
def start():
    print(cipher, "index:", codeindex)
    x = input("Type plus, minus, print (or quit):" )
    if x == "plus":
        encode()
    if x == "minus":
        decode()
    if x == "print":
        printX()
    if x == "quit":
        quitoK()
    else:
        start()
    
start()
