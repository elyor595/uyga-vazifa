import os
os.system('cls')
xarf = str(input('Xarf yoki belgi yoki raqam kiriting kiriting: '))

if xarf == '1' or xarf == '2' or xarf == '3' or xarf == '4' or xarf == '5' or xarf == '6' or xarf == '7' or xarf == '8' or xarf == '9' or xarf == '0':
    print("Raqam ")
elif  xarf == '!' or xarf == '@' or xarf == '#' or xarf == '$' or xarf == '%' or xarf == '^' or xarf == '&' or xarf == '*' or xarf == '.' or xarf == '_' or xarf == '+' or xarf == '=' or xarf == '`' or xarf == '~' or xarf == '<' or xarf == '>' or xarf == ';' or xarf == ':' or xarf == '{}' or xarf == '[]' :
    print("Belgi ")
else :
    print("Xarf ")