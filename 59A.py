def output(word: str) -> str:
    diff = 0
    for letter in word:
        if letter.isupper():
            diff += 1
        else:
            diff -= 1

    if diff > 0:
        return word.upper()

    return word.lower()


if __name__ == '__main__':
    word = input()

    answer = output(word)
    print(answer)
