# This implementation is not tested.

def read_data(fielname):
    f = open(fielname, "r")
    numVariables, numExpressions = list(map(int, f.readline().split()))
    expressions = [list(map(int, f.readline().split())) for i in range(numExpressions)]
    f.close()
    return numVariables, expressions


def assignValToF(F, x, val):
    newF = []
    for i in F:
        if x in i:
            if val == 1:
                continue
            else:
                i.remove(x)
                newF.append(i)
        elif -x in i:
            if val == 1:
                i.remove(-x)
                newF.append(i)
            else:
                continue
        else:
            newF.append(i)
    return newF


def solveSat(F):
    if len(F) == 0:
        return True
    for i in F:
        if len(i) == 0:
            return False
    x = abs(F[0][0])
    return solveSat(assignValToF(F, x, 0)) or solveSat(assignValToF(F, x, 1))


numVariables, expressions = read_data('./tests/1')

x = solveSat(expressions)

print(x)
