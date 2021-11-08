def ap(cost: int, cash: int, quantity: int) -> int:
    total_price = (cost + cost * quantity) * quantity / 2

    should_borrow = cash - total_price

    if should_borrow >= 0:
        return 0

    return abs(should_borrow)


if __name__ == '__main__':
    """
    arithmetic progression
    k cost of the first banana
    n initial number of dollars the soldier has
    w number of bananas he wants
    """
    [k, n, w] = map(int, input().strip().split(' '))

    answer = int(ap(k, n, w))
    print(answer)
