import math


def mininumPassengers(stops: str, passengers: list):
    inside = 0
    _max = -math.inf

    for i in range(stops):
        inside -= passengers[i][0]
        inside += passengers[i][1]
        _max = max(_max, inside)

    return _max


if __name__ == '__main__':
    stops = int(input())
    passengers = [list(map(int, input().split(' '))) for _ in range(stops)]

    answer = mininumPassengers(stops, passengers)
    print(answer)
