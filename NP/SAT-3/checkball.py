# This implementation is not tested.

def read_data(fielname):
    f = open(fielname, "r")
    numVariables, numExpressions = list(map(int, f.readline().split()))
    expressions = [list(map(int, f.readline().split())) for i in range(numExpressions)]
    f.close()
    return numVariables, expressions


def isSatisfy(F, alfa):
    unsatisfiedClause = []
    for f in F:
        for x in f:
            if x > 0 and alfa[x] == 1 or x < 0 and alfa[-x] == 0:
                break
        else:
            if len(unsatisfiedClause) == 0:
                unsatisfiedClause = f
    return unsatisfiedClause == [], unsatisfiedClause


def checkBall(F, alfa, r):
    satisfiable, unsatisfiedClause = isSatisfy(F, alfa)
    if satisfiable:
        return alfa
    if r == 0:
        return "not found"
    alfa_changing_index = [abs(i) for i in unsatisfiedClause]
    alfa_changed = [alfa[:i] + [1 ^ alfa[i]] + alfa[i + 1:] for i in alfa_changing_index]
    for newAlfa in alfa_changed:
        val = checkBall(F, newAlfa, r - 1)
        if val != "not found":
            return val
    return "not found"


def solveSat(n, F):
    initialAlfa0 = [0 for _ in range(n+1)]
    x = checkBall(F, initialAlfa0, n // 2 + 1)
    if x != "not found":
        return x
    initialAlfa1 = [0 for _ in range(n+1)]
    x = checkBall(F, initialAlfa1, n // 2 + 1)
    return x


numVariables, expressions = read_data('./tests/2')
x = solveSat(numVariables, expressions)

print(x)
