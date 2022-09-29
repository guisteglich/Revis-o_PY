"""
Transforme a brincadeira da figura abaixo em um programa que gera o “nome japonês” automaticamente:
"""

dic = {"a": "ka", "b": "tu", "c": "mi", "d": "te", "e": "ku", 
        "f": "lu", "g": "ji", "h": "ri", "i": "ki", "j": "zu",
        "k": "me", "l": "ta", "m": "rin", "n": "to", "o": "mo",
        "p": "no", "q": "ke", "r": "shi", "s": "ari", "t": "chi",
        "u": "do", "v": "ru", "x": "na", "w": "mei", "y": "fu",
        "z": "ra" }

def f(name):
    jp_name = ''
    for elem in name:
        jp_name = jp_name + dic[elem]
    return jp_name

print(f("gabe"))
print(f("guilherme"))