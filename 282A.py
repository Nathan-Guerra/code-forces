def bit(operations):
    x = 0
    for operation in operations:
        if '--' in operation:
            x -= 1
        elif '++' in operation:
            x += 1
    return x


if __name__ == '__main__':
    count_operations = int(input())
    operations = [input() for _ in range(count_operations)]
    print(bit(operations))
