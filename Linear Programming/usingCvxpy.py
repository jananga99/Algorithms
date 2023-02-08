# python3

import cvxpy as cp


def solve_diet_problem(n, m, A, b, c):
    x = cp.Variable(m)
    constraints = [x[i] >= 0 for i in range(m)] + [sum(A[i][j] * x[j] for j in range(m)) <= b[i] for i in range(n)]
    # for i in range(m + n):
    #     print("Constraint", i, ": ", str(constraints[i]))
    # print(sum(c[i] * x[i] for i in range(m)))
    obj = cp.Maximize(sum(c[i] * x[i] for i in range(m)))
    prob = cp.Problem(obj, constraints)
    result = prob.solve()
    # print(result)
    # # Print solution
    print("Optimal solution is: x = ", x.value)
    print("Optimal value is: ", prob.value)
    t = None
    if x.value is not None:
        t = 0
    elif prob.value == float('inf'):
        t = 1
    elif prob.value == -float('inf'):
        t = -1
    return t, x.value


filename = "./tests/02"
# filename = "./tests/02"
f = open(filename, "r")
n, m = list(map(int, f.readline().split()))
A = []
for i in range(n):
    A += [list(map(int, f.readline().split()))]
b = list(map(int, f.readline().split()))
c = list(map(int, f.readline().split()))

anst, ansx = solve_diet_problem(n, m, A, b, c)
if anst == -1:
    print("No solution")
if anst == 0:
    print("Bounded solution")
    print(' '.join(list(map(lambda x: '%.18f' % x, ansx))))
if anst == 1:
    print("Infinity")
