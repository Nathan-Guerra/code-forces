
def compareStrings(first_string, second_string):
    for i in range(len(first_string)):
        if first_string[i] > second_string[i]:
            return 1
        if second_string[i] > first_string[i]:
            return -1

    return 0


if __name__ == '__main__':
    first_string = input().lower()
    second_string = input().lower()

    print(compareStrings(first_string, second_string))
