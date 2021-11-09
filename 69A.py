class Body:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.z = 0

    def apply_coordinates(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z

    def is_in_equilibrium(self):
        return 'YES' if self.x == 0 and self. y == 0 and self.z == 0 else 'NO'


if __name__ == '__main__':
    n = int(input())
    body = Body()
    for i in range(n):
        [x, y, z] = map(int, input().split(' '))
        body.apply_coordinates(x, y, z)

    answer = body.is_in_equilibrium()

    print(answer)
