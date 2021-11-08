def next_level(limiter, participants_scores):
    limiter_score = int(participants_scores[int(limiter) - 1])

    can_pass = 0
    for participant_score in participants_scores:
        participant_score = int(participant_score)
        if participant_score >= limiter_score and participant_score > 0:
            can_pass += 1

    return can_pass


if __name__ == '__main__':
    total_participants, limiter = input().split(' ')
    participants_scores = input().split(' ')

    print(next_level(limiter, participants_scores))
