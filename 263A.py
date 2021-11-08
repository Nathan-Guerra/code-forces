def adjust_placement(matrix):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == 1:
                """
                    retorna o valor absoluto entre a diferença
                    da posição atual do 1 e o centro da matriz.
                    Isso resulta na quantidade de deslocamentos
                    de linhas e colunas para centralizar o número
                """
                return abs(row-2) + abs(col-2)


if __name__ == '__main__':
    matrix = []

    # 5x5
    for i in range(5):
        matrix.append([j for j in map(int, input().split(' '))])

    print(adjust_placement(matrix))
