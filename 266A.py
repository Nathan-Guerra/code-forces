def differentNeighbors(total_stones: int, stones: str) -> int:
    removed = 0

    for i in range(0, total_stones - 1):
        if (stones[i] == stones[i+1]):
            removed += 1

    return removed


if __name__ == '__main__':
    total_stones = int(input())
    stones = input()

    noEqualNeighbors = differentNeighbors(total_stones, stones)
    print(noEqualNeighbors)
