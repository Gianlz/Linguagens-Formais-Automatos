def algoritmocyk(e_string):
    tam_entrada = len(e_string)

    # Tabela CYK
    tabela_cyk = [[[] for _ in range(tam_entrada)] for _ in range(tam_entrada)]

    # Preenchimento das células da diagonal principal
    for i in range(tam_entrada):
        terminal = e_string[i]
        producoes = []

        # Verificar se algum não-terminal gera o símbolo terminal
        if terminal == 'a':
            producoes.append('A')
        elif terminal == 'b':
            producoes.append('B')

        tabela_cyk[i][i] = producoes

    # Preenchimento das células restantes
    for tam in range(2, tam_entrada + 1):
        for inicio in range(0, tam_entrada - tam + 1):
            fim = inicio + tam - 1
            producoes = []

            for k in range(inicio, fim):
                esq_productions = tabela_cyk[inicio][k]
                dir_productions = tabela_cyk[k + 1][fim]

                # Verificar combinações de produções possíveis
                for esq in esq_productions:
                    for i in dir_productions:
                        # Verificar regras de produção da gramática
                        if esq == 'S' and i == 'A':
                            producoes.append('U')
                        if esq == 'S' and i == 'B':
                            producoes.append('T')
                        if (esq == 'A' and i == 'T') or (esq == 'B' and i == 'U') or (
                                esq == 'X' and i == 'X') or (esq == 'A' and i == 'B') or (
                                esq == 'B' and i == 'A'):
                            producoes.append('X')
                        if (esq == 'A' and i == 'T') or (esq == 'B' and i == 'U') or (
                                esq == 'X' and i == 'X') or (esq == 'A' and i == 'B') or (
                                esq == 'B' and i == 'A'):
                            producoes.append('S')

            tabela_cyk[inicio][fim] = producoes

    # Verificar se o símbolo inicial está na célula final
    return 'S' in tabela_cyk[0][tam_entrada - 1]


# Entrada
entrada = 'aabb'

if entrada == '' or entrada == 'ε' or entrada == 'vazio':
    entrada = 'ε'
    print("A cadeia = {0}\nÉ aceita pela gramática.".format(entrada))
elif algoritmocyk(entrada):
    print("A cadeia = {0}\nÉ aceita pela gramática.".format(entrada))
else:
    print("A cadeia = {0}\nNÃO é aceita pela gramática.".format(entrada))
