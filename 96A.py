def solution(players: str) -> str:
    current_chain = players[0]
    player_stack = 0

    for player in players:
        if (player == current_chain):
            player_stack += 1
            if player_stack >= 7:
                return 'YES'
        else:
            current_chain = player
            player_stack = 1

    return 'NO'


if __name__ == '__main__':
    players = input()

    answer = solution(players)
    print(answer)
