import functools


def solve(solutions):
    implemented_solutions = 0
    for s in solutions:
        majority = functools.reduce(
            lambda increments, current: increments + int(current), s, 0)

        if majority >= 2:
            implemented_solutions += 1

    return implemented_solutions


if __name__ == '__main__':
    problems = int(input())

    solutions = [
        input().split(' ') for _ in range(problems)

    ]

    print(solve(solutions))
