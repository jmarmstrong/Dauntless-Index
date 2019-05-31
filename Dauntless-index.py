import time
import os
loop = True
def pp(text):
    print(text)
while loop:
    pp("Hello and welcome to the Dauntless Behemoth Index")
    pp("""
    1) Neutral
    2) Blaze
    3) Frost
    4) Shock
    5) Radiant
    6) Umbral
       """,)
    variable = input("Please enter the number of the type of Behemoth ")
    if variable == "1":
        loop = False
        pp("""
    1) Gnasher
    2) Quillshot
    3) Shrike
    """)
    neutral = input("Please enter the number of the behemoth") 
    if neutral == "1":
        pp("""
1) Lesser Gnasher
2) Gnasher
3) Ragetail Gnasher
""")
        gnasher = input("Please enter the number for the type of Gnasher")
        if gnasher == "1":
            g = open("lgnasher.txt", "r") #https://www.guru99.com/reading-and-writing-files-in-python.html
            if g.mode == "r":
                contents = g.read()
                print(contents)
                yn = input("do you want to return to the beginning Y/N: ")
                if yn == "Y" or yn == "y":
                    loop = True
                if yn == "N" or yn == "n":
                    exit()
                    
        if gnasher == "2":
            g = open("gnasher.txt", "r")
            if g.mode == "r":
                contents = g.read()
                print (contents)
                yn = input("do you want to return to the beginning Y/N: ")
                if yn == "Y" or yn == "y":
                    loop = True
                if yn == "N" or yn == "n":
                    exit()
                    
        if gnasher == "3":
            g = open("rgnasher.txt", "r")
            if g.mode == "r":
                contents = g.read()
                print (contents)
                yn = input("do you want to return to the beginning Y/N: ")
                if yn == "Y" or yn == "y":
                    loop = True
                if yn == "N" or yn == "n":
                    exit()
                
    if neutral == "2":
        q = open("quillshot.txt", "r")
            if q.mode == "r":
                contents = q.read()
                print (contents)
                yn = input("do you want to return to the beginning Y/N: ")
                if yn == "Y" or yn == "y":
                    loop = True
                if yn == "N" or yn == "n":
                    exit()
                    
    if neutral == "3":
        q = open("shrike.txt", "r")
            if q.mode == "r":
                contents = q.read()
                print (contents)
                yn = input("do you want to return to the beginning Y/N: ")
                if yn == "Y" or yn == "y":
                    loop = True
                if yn == "N" or yn == "n":
                    exit()
                    
                    
    if variable == "Blaze" or variable ==  "blaze":
        loop = False
        pp("Hi")
    if variable == "Frost" or variable ==  "frost":
        loop = False
        pp("Hi")
    if variable == "Shock" or variable ==  "shock":
        loop = False
        pp("Hi")
    if variable == "Radiant" or variable ==  "radiant":
        loop = False
        pp("Hi")
    if variable == "Umbral" or variable == "umbral":
        loop = False
        pp("Hi")
