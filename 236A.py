def shouldChat(name: str) -> str:
    different_letters = []

    for letter in name:
        if letter not in different_letters:
            different_letters.append(letter)

    result = len(different_letters) % 2

    if result == 0:
        return 'CHAT WITH HER!'

    return 'IGNORE HIM!'


if __name__ == '__main__':
    name = input()

    should_chat = shouldChat(name)
    print(should_chat)
