# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 18:11:11 2019

@author: thoma
"""
import time
codeindex = 0
stringlist = []

#cipher input.
cipher1_input = input("Type in cipher1 here:" )
cipher2_input = input("Type in cipher2 here:" )
cipher3_input = input("Type in cipher3 here:" )
cipher = (int(cipher1_input),int(cipher2_input),int(cipher3_input))

def encode():
    global stringlist
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
    global stringlist
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
    global stringlist
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
    f.close()
    start()

def quitoK():
    quit()
    time.sleep(1)
    return()
    quitoK()
    
def start():
    global stringlist
    print("stringlist:",stringlist)
    print("cipher:",cipher, "index:", codeindex)
    print("Type:")
    print("+ for add index (cipher)") 
    print("- for deduct index (cipher)")
    print("p to print out stored string to export.txt")
    print("i to import a string from export.txt")
    print("s to input your own string.")
    print("q to quit")
    x = input("Type here:" )
    if x == "s":
        stringlist.clear()
        string_input = input("Type in string here:" )
        for i in string_input:
            stringlist.append(ord(i))
        start()
    if x == "i":
        stringlist.clear()
        f1 = open("export.txt","r")
        string_input = f1.read()
        for i in string_input:
            stringlist.append(ord(i))
        f1.close()
        start()
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
