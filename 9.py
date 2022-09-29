"""Faça um programa que recebe uma sequência genética de aminoácidos
na forma de uma string longa com as letras A, C, G, T 
(por exemplo “ACGAATTCCGCGAATTC”) e retorna todas as substrings
 de exatamente 10 aminoácidos que se repete pelo menos uma vez."""

def f(st):
    l_final = []
    length = len(st)
    while length > 10:
        c = ""
        for i in range(0, 10):
            c = c + st[i]
        length-=10
        l_final.append(c)
    return l_final

print(f("ACGAATTCCGCGAATTC"))
print(f("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))