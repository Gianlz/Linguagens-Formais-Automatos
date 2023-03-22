import re

def automato(entrada):
    estados = [
        {
            '[a-eghj-vx-z]': 1,
            '[0-9]': 4,
            'i': 2,
            'f': 5,
            'w': 8
        },
        {
            '[a-z]': 1,
            '[0-9]': 1
        },
        {
            '[^f]': 1,
            'f': 3
        },
        {
            '[a-z]': 1
        },
        {
            '[a-z]': 99,
            '[0-9][^a-z]': 4
        },
        {
            '[^o]': 1,
            'o': 6
        },
        {
            '[^r]': 1,
            'r': 7
        },
        {
            '[a-z]': 1
        },
        {
            '[^h]': 1,
            'h': 9
        },
        {
            '[^i]': 1,
            'i': 10
        },
        {
            '[^l]': 1,
            'l': 11
        },
        {
            '[^e]': 1,
            'e': 12
        },
        {
            '[a-z]': 1
        },
        {
            'Estado para escape'
        }
    ]

    estado_atual = 0
    cadeia_atual = ''

    for i in range(len(entrada)):
        char = entrada[i]

        if estado_atual >= len(estados):
            return f'{entrada} Cadeia não reconhecida'

        for regex, prox in estados[estado_atual].items():
            if re.match(f'^{regex}$', char):
                estado_atual = prox
                cadeia_atual = char + cadeia_atual
                break

    finais = {
        1: 'id',
        3: 'palavra reservada IF',
        4: 'constante',
        7: 'palavra reservada FOR',
        12: 'palavra reservada WHILE'
    }

    if estado_atual in finais:
        return f'{entrada} - Cadeia aceita como:  [{finais[estado_atual]}]'
    else:
        return f'{entrada} - Cadeia não reconhecida'


print(automato('gian69'))
print(automato('69pedro'))
print(automato('while'))
print(automato('1337'))
print(automato('gianluca'))
print(automato('for'))
print(automato('if'))
print(automato("4y"))
