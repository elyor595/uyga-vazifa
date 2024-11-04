import os
os.system('cls')

'''
a = 123 ; b = 23

if a > b:
    print("Katta A ", a)
else:
    print("Katta B ", b)'''
    
'''    
son = int(input("Son: "))

if son > 0:
    print("Musfat ")
elif son < 0:
    print("Manfiy ")
else :
    ("Nomalum")'''
'''
son = int(input("Son: "))
n = int(input("n: "))
raqam = int(input("raqam: "))

if son > n and son > raqam:
    print(son)
elif n > son and n > raqam:
    print(n)
elif raqam > son and raqam > n:
    print(raqam)
    
if son < n and son < raqam:
    print(son)
elif n < son and n < raqam:
    print(n)
elif raqam < son and raqam < n:
    print(raqam)'''
    
'''   
son = str(input("Rang: "))


if son == 'qizil':
    print("Toxtang")
elif son == 'sariq':
    print("Tayyorlaning ")
elif son == 'yashil':
    print("Yuring")'''
'''    
son = int(input("yosh kiriting: "))


if son < 7:
    print("Bepul")
elif son > 8 and son < 18:
    print("1500")
elif son > 19:
    print("2500")'''
'''   

#####################'//////////////////////////////////////////
son = int(input("N: "))


if son == 1:
    print("%10")
elif son == 2:
    print("%15")
elif son > 2:
    print("%20")'''
    
'''   
son = str(input("Model: "))


if son == 'damas':
    print("100 mln")
elif son == 'spark':
    print("90 mln")
elif son == 'kaptiva':
    print("300 mln") 
elif son == 'nexia':
    print("125 mln")
elif son == 'malibu':
    print("400 mln")'''
    
'''   
son = int(input("Son: "))
n = int(input("n: "))
raqam = int(input("raqam: "))

if son > n and son > raqam:
    print(son)
elif n > son and n > raqam:
    print(n)
elif raqam > son and raqam > n:
    print(raqam) '''   
'''   
son = int(input("Son: "))

if son % 3 == 0:
    print("Bo'linadi")
else:
    print("Bo'linmaydi")'''
    
''' 
son = int(input("Son: "))

if son > 0:
    print("+5")
elif son < 0:
    print("-5")
else:
    print("5")'''
    
'''  
son = int(input("Son: "))

raqam = son % 10

if raqam % 2 == 0:
    print("Juft")
else:
    print("Toq")'''
    

'''
son = int(input("son: "))
n = (son // 10) % 10
raqam = (son // 100) % 10
son = n * raqam
if son % 2 == 0 and son % 5 == 0:
    print("A")
if son % 3 == 0 and son % 7 == 0:
    print("B")
else:
    print("bolinmaydi")'''


'''
son = int(input("Son: "))

if son > 0:
    print("Musfat ")
elif son < 0:
    print("Manfiy ")
else :
    ("Nomalum")'''
'''    
son = int(input("Son: "))

if son % 2 ==0:
    print("Juft ")
elif son % 2 != 0:
    print("toq ")
else :
    ("Nomalum")'''
    
a,b,c,d,e = map(int , input("5 ta son probel kiriting").splip())
