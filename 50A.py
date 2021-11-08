def dominoes_amount(row, column):
    return row * column // 2


if __name__ == '__main__':
    row, column = map(int, input().split(' '))
    print(dominoes_amount(row, column))
