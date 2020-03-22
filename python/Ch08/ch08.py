import eightQueens


def triple_step(n):
    if 1 == n:
        return 1

    if 2 == n:
        return 2
    if n == 3:
        return 1 + 2 + 1
    return triple_step(n - 1) + triple_step(n - 2) + triple_step(n - 3)


def superset(st, subsets=[[]]):
    if st is []:
        return subsets

    for i in len(st):
        subsets.append(st[:i] + st[:i + 1])
    return superset(st[1:], subsets.append(st[0]))


def mult_recorsive(a, b, suffix=0):
    if b == 0:
        return 0
    if b is 1:
        return a + suffix
    if b % 2 == 0:
        return mult_recorsive(a + a, b >> 1, 0)
    return mult_recorsive(a, b - 1, a)


def CH08_tester():
    None


def eight_queens_tester():
    for x in range(9):
        eightQueens.eight_queens_solver(x)


eight_queens_tester()
