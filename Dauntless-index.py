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
        loop2 = False
        while loop2:
            loop = False
            pp("""
        1) Gnasher
        2) Quillshot
        3) Shrike
        """)
            neutral = input("Please enter the number of the behemoth")
    else:
        loop = True
        
        if neutral == "1":
                while loop3:
                    pp("""
            1) Lesser Gnasher
            2) Gnasher
            3) Ragetail Gnasher
            """)
                    gnasher = input("Please enter the number for the type of Gnasher")
                    if gnasher == "1":
                        while loop4:
                            g = open("lgnasher.txt", "r") #https://www.guru99.com/reading-and-writing-files-in-python.html
                            if g.mode == "r":
                                contents = g.read()
                                print(contents)
                                yn = input("do you want to return to the beginning Y/N: ")
                                if yn == "Y" or yn == "y":
                                    loop = True
                                else:
                                    loop4 = True
                                if yn == "N" or yn == "n":
                                    exit()
                                else:
                                    loop4 = True
                    else:
                        loop3 = True
                                
                    if gnasher == "2":
                        while loop5:
                            g = open("gnasher.txt", "r")
                            if g.mode == "r":
                                contents = g.read()
                                print (contents)
                                yn = input("do you want to return to the beginning Y/N: ")
                                if yn == "Y" or yn == "y":
                                    loop = True
                                else:
                                    loop5 = True
                                if yn == "N" or yn == "n":
                                    exit()
                                else:
                                    loop5 = True
                    else:
                        loop3 = True
                        
                    if gnasher == "3":
                        while loop6:
                            g = open("rgnasher.txt", "r")
                            if g.mode == "r":
                                contents = g.read()
                                print (contents)
                                yn = input("do you want to return to the beginning Y/N: ")
                                if yn == "Y" or yn == "y":
                                    loop = True
                                else:
                                    loop6 = True
                                if yn == "N" or yn == "n":
                                    exit()
                                else:
                                    loop6 = True
                    else:
                        loop3 = True
        else:
            loop2 = True
            
    if neutral == "2":
        while loop7:
            q = open("quillshot.txt", "r")
            if q.mode == "r":
                    contents = q.read()
                    print (contents)
                    yn = input("do you want to return to the beginning Y/N: ")
                    if yn == "Y" or yn == "y":
                        loop = True
                    else:
                        loop7 = True
                    if yn == "N" or yn == "n":
                        exit()
                    else:
                        loop7 = True
    else:
        loop2 = True
                                
    if neutral == "3":
        while loop8:
            loop2 = False
            q = open("shrike.txt", "r")
            if q.mode == "r":
                    contents = q.read()
                    print (contents)
                    yn = input("do you want to return to the beginning Y/N: ")
                    if yn == "Y" or yn == "y":
                        loop = True
                    else:
                        loop8 = True
                    if yn == "N" or yn == "n":
                        exit()
                    else:
                        loop8 = True
    else:
        loop2 = True
                    
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

    
