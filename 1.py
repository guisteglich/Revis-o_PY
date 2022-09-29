"""
Crie uma função que recebe dois números inteiros e retorna o produto,
mas caso o produto seja maior que 1000, retorna a soma.
"""

def f(a, b):
    if (a * b) <= 1000:
        return a * b
    return a + b


print(f(2, 1001))