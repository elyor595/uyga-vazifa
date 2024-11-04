import os
os.system('cls')
son = int(input('son'))
sum = 0
if son % 3 ==0 and son % 5 == 0 and son % 7 == 0:
    print("Bolinadigan sonni 2 ga kopaytirib chiqardi",son * 2)
else :
    print("Bolinadigan sonlar yoq")