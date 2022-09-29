"""
Faça uma função que recebe duas listas de igual tamanho e 
retorna um conjunto de tuplas dos pares de elementos na mesma posição em cada lista.
"""

# def f(l1, l2):
#     tup = []
#     l = [0, 0]
#     for i in range (0, len(l1)):
#         l[0] = l1[i]
#         l[1] = l2[i]
#         tup.append(l)
#     return tup

def f(l1, l2):
    
    li = list()
    for i in range(0, len(l1)):
        tup = [0, 0]
        
        tup[0] = l1[i]
        tup[1] = l2[i]

        li.append(tup)
    return li

l1 = [1, 2, 4]
l2 = [4, 2, 1]

print(f(l1, l2))