def response(limak_w: int, bob_w: int) -> int:
    years = 0

    while limak_w <= bob_w:
        limak_w *= 3
        bob_w *= 2
        years += 1

    return years


if __name__ == '__main__':
    [limak_w, bob_w] = map(int, input().split(' '))

    answer = response(limak_w, bob_w)
    print(answer)
