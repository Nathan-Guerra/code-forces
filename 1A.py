import math


def solution(n: int, m: int, a: int) -> int:
    return math.ceil(n/a) * math.ceil(m/a)


if __name__ == '__main__':
    [n, m, a] = map(int, input().split(' '))

    answer = solution(n, m, a)
    print(answer)
