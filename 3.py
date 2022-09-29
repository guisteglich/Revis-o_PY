"""
Escreva uma função que, recebendo um número inteiro n, 
e retorne os n primeiros números da sequência de Fibonacci.
"""

"1, 1, 2, 3, 5, 8"

def n_fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n_fib(n-1) + n_fib(n-2)

t = 5
for i in range(0, t+1):
    print(n_fib(i))