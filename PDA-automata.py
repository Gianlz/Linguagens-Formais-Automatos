import re

# Define uma classe PDA
class PDA:
    def __init__(self):
        self.stack = []
        # Define os estados e transições para o PDA
        self.estados = [
            {
                'X': [(1, 'X')],
                '[^ab]': [(33, '')],
                '[ab]': [(0, '')]
            },
            {
                '[^ab]': [(33, '')],
                '[ab]': [(1, '')]
            }
        ]

    # Define uma função para empilhar um símbolo na pilha
    def push(self, simbulo):
        self.stack.append(simbulo)

    # Define uma função para desempilhar um símbolo da pilha
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

    # Define uma função para processar a string de entrada
    def automato(self, entrada):
        estado_atual = 0
        cadeia_atual = ''
        for i in range(len(entrada)):
            char = entrada[i]

            # Verifica se o comprimento da string de entrada é par
            if len(entrada) % 2 == 0:
                return f"{entrada} Cadeia não reconhecida"

            # Verifica se o estado atual é válido
            if estado_atual >= len(self.estados):
                return f'{entrada} Cadeia não reconhecida'

            # Itera sobre as transições para o estado atual
            for regex, transicoes in self.estados[estado_atual].items():
                if estado_atual != 1 and char != 'X':
                    # Se o caractere corresponder à transição atual, atualize o estado e empilhe um símbolo na pilha
                    if re.match(f'^{regex}$', char):
                        estado_atual, push_symbol = transicoes[0]
                        self.push(push_symbol)
                        cadeia_atual = char + cadeia_atual
                        break
                else:
                    # Se o caractere for 'X', atualize o estado
                    if char == 'X':
                        estado_atual, _ = transicoes[0]
                        break
                    else:
                        # Se a string de entrada restante for menor que a string atual, desempilhe símbolos da pilha e atualize a string atual
                        if len(entrada[i + 1:]) != len(cadeia_atual):
                            for x in cadeia_atual:
                                if x != entrada[i]:
                                    return f'{entrada} Cadeia não reconhecida'
                                else:
                                    self.pop()
                                    cadeia_atual = cadeia_atual[1:]
                                    break
                            break
                        else:
                            return f'{entrada} Cadeia não reconhecida'

        # Define os estados finais para o PDA
        finais = {
            1: 'Formato (wXwr)'
        }
        # Verifica se o estado atual é um estado final
        if estado_atual in finais:
            return f'{entrada} - Cadeia aceita como:  [{finais[estado_atual]}]'
        else:
            return f'{entrada} - Cadeia não reconhecida'


# Cria uma nova instância da classe PDA
pda = PDA()

# Recebe a entrada do usuário e processa-a usando o PDA
palavra = str(input("Digite sua palavra: "))
print(pda.automato(palavra))
