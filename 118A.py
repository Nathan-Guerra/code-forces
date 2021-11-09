def solution(s: str) -> str:
    arr = []

    for letter in s:
        # it is a consonant
        if letter.upper() not in ['A', 'O', 'Y', 'E', 'U', 'I']:
            arr.append(letter.lower())

    return '.' + '.'.join(arr)


if __name__ == '__main__':
    s = input()

    answer = solution(s)
    print(answer)
