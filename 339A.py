def rearrangeSum(disorganized: str) -> str:
    values = disorganized.split('+')

    for i in range(len(values)):
        for j in range(i, len(values)):
            if values[i] > values[j]:
                aux = values[i]
                values[i] = values[j]
                values[j] = aux
    return '+'.join(values)


if __name__ == '__main__':
    _sum = input()

    organizedSum = rearrangeSum(_sum)
    print(organizedSum)
