"""
Escreva um programa capaz de gerar o padrão abaixo utilizando laços.
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5.
"""

def f(t):
    for i in range(1, t+1):
        c = ""
        cnt = i
        while cnt != 0:
            c = c + str(i) + " "
            cnt -= 1
        print (c)
f(5)
