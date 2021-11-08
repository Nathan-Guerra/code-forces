def response(n: int, k: int) -> int:
    for i in range(k):
        if n % 10 == 0:
            n /= 10
        else:
            n -= 1

    return int(n)


if __name__ == '__main__':
    [n, k] = map(int, input().split(' '))

    answer = response(n, k)
    print(answer)
