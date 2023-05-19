# Gianluca Zugno

def automato(entrada):
    stack = []
    i = 0

    # Empilhe os símbolos 'a' e 'b'
    while i < len(entrada) and entrada[i] in ['a', 'b']:
        stack.append(entrada[i])
        i += 1

    # Verifique se o próximo símbolo é 'X'
    if i < len(entrada) and entrada[i] == 'X':
        i += 1
    else:
        return "Cadeia não reconhecida"

    # Desempilhe e compare com a entrada
    while i < len(entrada) and stack:
        if entrada[i] == stack[-1]:
            stack.pop()
        else:
            return "Cadeia não reconhecida"
        i += 1


    # Verifique se a pilha está vazia e a entrada foi totalmente processada
    if not stack and i == len(entrada):
        return "Cadeia aceita"
    else:
        return "Cadeia não reconhecida"

print(automato("abXba"))  # Cadeia aceita
print(automato("aXa"))    # Cadeia aceita
print(automato("abXab"))  # Cadeia não reconhecida
print(automato("abab"))   # Cadeia não reconhecida


