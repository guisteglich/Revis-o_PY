"""
 Escreva um programa que seja capaz de unir esses dois dicionários abaixo em um único dicionário.
 d1 = {'Dez': 10, 'Vinte': 20, 'Trinta': 30}
d2 = {'Trinta': 30, 'Quarenta': 40, 'Cinquenta': 50}
"""

d1 = {'Dez': 10, 'Vinte': 20, 'Trinta': 30}
d2 = {'Trinta': 30, 'Quarenta': 40, 'Cinquenta': 50}


new = {**d1, **d2}
print(new)