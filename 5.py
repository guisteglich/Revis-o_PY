"""
Escreva uma função que recebe uma lista e 
retorna um dicionário representando quantas vezes cada elemento aparece na lista.
"""
def f(l):
    d = {}
    for i in range(0, len(l)):
        c = l.count(l[i])
        d[l[i]] = c
    return d

lis = [1, 5, '6', 0, 0, 0, 1, 'i']    
di = ["a", "b", "c", "c"]
print(f(lis))


