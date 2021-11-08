class QueuePosition:
    def __init__(self, student) -> None:
        self.student = student
        self.should_swap = False

    def swap(self) -> None:
        if self.student == 'B':
            self.student = 'G'
        elif self.student == 'G':
            self.student = 'B'


def orderQueue(n: int, t: int, queue: str) -> str:
    arrangement = list(map(lambda student: QueuePosition(student), queue))

    for _ in range(t):
        for j in range(0, n-1):
            if (arrangement[j].student == 'B' and
                    arrangement[j+1].student == 'G'):
                arrangement[j+1].should_swap = True
                arrangement[j].should_swap = True

        for student in arrangement:
            # swap students positions after completing the scan
            if student.should_swap:
                student.swap()

            student.should_swap = False

    answer = ''

    for student in arrangement:
        answer += student.student

    return answer


if __name__ == '__main__':
    [n, t] = map(int, input().split(' '))
    queue = input()

    answer = orderQueue(n, t, queue)
    print(answer)
