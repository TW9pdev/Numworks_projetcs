import re
from math import*

b16 = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]

var = int(input())
var_16 = var
stock_var = var
data = var
final = 0

def base2():

    global var
    global data
    liste = list(str(var))
    stock = []

    while var != 0:
        if var % 2 == False:
            var /= 2
            stock += list(str(0))
        else:
            var -= 1
            var /= 2
            stock += list(str(1))


    reversed_stock = stock[::-1]
    reversed_stock = str(reversed_stock)
    pattern = re.sub("[^0-9]", "", reversed_stock)
    print(stock_var, "s'écrit", pattern, "en base 2 (binaire).")

def base16():

    global var_16
    global data
    stock = []

    if var_16 <= 15:
        data = b16[var_16]
    else:
        while var_16 != 0:
            data = var_16 % 16
            var_16 = var_16 // 16
            
            stock.append(b16[data])

    reversed_number = stock[::-1]
    reversed_number = str(reversed_number)
    pattern = re.sub("[^0-9A-Z]", "", reversed_number)
    print(stock_var, "s'écrit", pattern, "en base 16 (héxadécimal).")

    
base2()
base16()