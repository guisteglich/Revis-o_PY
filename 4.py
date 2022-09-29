"""
Crie uma função que, recebendo como argumento uma lista e um número, 
adicione o número ao final da lista apenas se a lista ainda não contém aquele número.
"""

def f(l, n):
    if n not in l:
        l.append(n)
    return l

l = [1, 2, 4, 5, 6]
print(f(l, 5))
    


