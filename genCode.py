myList = " "
count = 0
with open("genCode/imports.txt","r") as c:
    myList += (c.read().replace("\n"," "))
    myList = myList.split()
    myListLen = len(myList)
    
with open("genCode/imports.txt","r") as c:


    with open("genCode/tester.py","w") as f:
        for i in range(myListLen):
            f.write(f'import {c.readline()}')
            
        f.write('\n')

with open("genCode/imports.txt","r") as c:
   
    with open("genCode/tester.py","a") as f:
        for i in range(myListLen):
            f.write(f'print({c.readline()}.__version__())'.replace("\n",""))
            f.write('\n') 




     