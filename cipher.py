# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 18:11:11 2019

@author: thoma
"""

codeindex = 0
stringlist = []

#cipher input.
cipher1_input = input("Type in cipher1 here:" )
cipher2_input = input("Type in cipher2 here:" )
cipher3_input = input("Type in cipher3 here:" )
cipher = (int(cipher1_input),int(cipher2_input),int(cipher3_input))

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
    f = open("export.txt","w+")
    for i in printy:
        f.write(i)
    chrlist.clear()
    start()
def quitoK():
    quit()
    
def start():
    global string_input
    global stringlist
    print("stringlist:",stringlist)
    print("cipher:",cipher, "index:", codeindex)
    print("Type + (for add index), - (for deduct index), p (to print string) or q (to exit)...")
    print("Or type i to import a string from export.txt")
    x = input("Type here:" )
    if x == 's':
        string_input = input("Type in string here:" )
        stringlist = []
        for i in string_input:
            stringlist.append(ord(i))
    if x == "i":
        f1 = open("export.txt","r")
        string_input = f1.read()
        for i in string_input:
            stringlist.append(ord(i))
    if x == "+":
        encode()
    if x == "-":
        decode()
    if x == "p":
        printX()
    if x == "q":
        quitoK()
    else:
        start()
start()
