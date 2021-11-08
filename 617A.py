import math


def steps(coordinate: int):
    steps = math.floor(coordinate / 5)

    if coordinate % 5 == 0:
        return steps

    return steps + 1


if __name__ == '__main__':
    coordinate = int(input())

    answer = steps(coordinate)
    print(answer)
