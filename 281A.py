def capitalize(target: str) -> str:
    capitalizedLetter = target[0].upper()

    return capitalizedLetter + target[1:]


if __name__ == '__main__':
    rawString = input()

    capitalizedString = capitalize(rawString)
    print(capitalizedString)
