import random
import numpy as np


class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


def ReadEquation(filename):
    f = open(filename, "r")
    # size = int(input())
    size = int(f.readline().split()[0])
    a = []
    b = []
    for row in range(size):
        # line = list(map(float, input().split()))
        line = list(map(float, f.readline().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)


# r <--- x*r
def rowDivide(r, a, x, b):
    size = len(a)
    for i in range(size):
        a[r][i] /= x
    b[r] /= x


def SelectPivotElement(a, used_rows, used_columns):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    size = len(a)
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
    while pivot_element.column < size and a[pivot_element.row][pivot_element.column] == 0:
        pivot_element.column += 1
    if pivot_element.column == size:
        raise Exception("No slutions")
    return pivot_element


def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[
        pivot_element.column]
    pivot_element.row = pivot_element.column


# r <--- r - a[r][pivotColumn] * pivotRow
def rowOpera(r, pivot_element, a, b):
    c = a[r][pivot_element.column]
    size = len(a)
    for i in range(size):
        a[r][i] = a[r][i] - c * a[pivot_element.row][i]
    b[r] = b[r] - c * b[pivot_element.row]


def ProcessPivotElement(a, b, pivot_element):
    # Write your code here
    size = len(a)
    rowDivide(pivot_element.row, a, a[pivot_element.row][pivot_element.column], b)
    for r in range(size):
        if r != pivot_element.row and a[r][pivot_element.column] != 0:
            rowOpera(r, pivot_element, a, b)


def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True


# Solve equations usinf Gaussian
def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)
    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)
    return b


def printAnswers(column, filename):
    size = len(column)
    f = open(filename, "w")
    for row in range(size):
        f.write("%.20lf\n" % column[row])
    f.close()


def writeRandomTests(nn, ll, ul, maxN):
    for i in range(nn):
        f = open("./random_tests/" + str(i), "w")
        n = random.randint(1, maxN)
        f.write(str(n) + "\n")
        for r in range(n):
            row = []
            for c in range(n + 1):
                row.append(random.randint(ll, ul))
            f.write(" ".join(map(str, row)))
            f.write("\n")
        f.close()


# Solves using np
def solveNp(equation):
    a = np.array(equation.a)
    b = np.array(equation.b)
    return np.linalg.solve(a, b)


# Gets absolute error for given two numbers
def absErr(a, b):
    return abs(a - b)


# Gets maximum relative error for given two numbers
def relErr(a, b):
    if a == b == 0:
        return 0
    if a == 0:
        return abs((a - b) / b)
    elif b == 0:
        return abs((a - b) / a)
    return max(abs((a - b) / a), abs((a - b) / b))


def err(a, b):
    return min(absErr(a, b), relErr(a, b))


# Compares numpy and this answer files and writes a simpele report into a ne file
def writeReport(n, filename1, filename2, outFile):
    f1 = open(filename1, "r")
    f2 = open(filename2, "r")
    f3 = open(outFile, "w")
    for i in range(n):
        x = float(f1.readline().split()[0])
        y = float(f2.readline().split()[0])
        e = err(x, y)
        if e <= 0.000001:
            f3.write("Success " + str(e) + "\n")
        else:
            print("Failture " + filename1 + " " + filename2)
            f3.write(str(e) + "\n")
    f1.close()
    f2.close()
    f3.close()


def writeNoSlo(ansName, outName):
    f1 = open(ansName, "w")
    f2 = open(outName, "w")
    f1.write("No solutions")
    f2.write("No solutions")
    f1.close()
    f2.close()


def solveTests(n):
    for i in range(n):
        equation = ReadEquation("./random_tests/" + str(i))
        ansName = "./random_tests/" + str(i) + "a"
        npname = "./random_tests/" + str(i) + "anp"
        outName = "./random_tests/" + str(i) + "rep"
        try:
            solution = SolveEquation(equation)
            printAnswers(solution, ansName)
            solution = solveNp(equation)
            printAnswers(solution, npname)
            writeReport(len(equation.a), ansName, npname, outName)
            # print("Success ",i)
        except:
            writeNoSlo(ansName, outName)


# Number of Tests
n = 1000
# upper and lower limits for elements of the matrix
ll = -100
ul = 100
# Upper limit for the matrix size
maxN = 5
writeRandomTests(n, ll, ul, maxN)
solveTests(n)
