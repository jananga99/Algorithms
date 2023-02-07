class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)


# r <--- x/r
def rowDivide(r, a, x, b):
    size = len(a)
    for i in range(size):
        a[r][i] /=x
    b[r]/=x

# r <--- r - a[r][pivotColumn] * pivotRow
def rowOpera(r, pivot_element, a, b):
    c = a[r][pivot_element.column]
    size = len(a)
    for i in range(size):
        a[r][i] = a[r][i] - c * a[pivot_element.row][i]
    b[r] = b[r] - c * b[pivot_element.row]

def SelectPivotElement(a, used_rows, used_columns):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    size = len(a)
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
    while pivot_element.row<size and a[pivot_element.row][pivot_element.column] == 0:
        pivot_element.row +=1
    if pivot_element.row == size:
        raise Exception("No slutions")
    return pivot_element


def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[
        pivot_element.column]
    pivot_element.row = pivot_element.column


def ProcessPivotElement(a, b, pivot_element):
    # Write your code here
    size = len(a)
    rowDivide(pivot_element.row, a, a[pivot_element.row][pivot_element.column], b)
    for r in range(size):
        if r!=pivot_element.row and a[r][pivot_element.column]!=0:

            rowOpera(r, pivot_element, a, b)


def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True


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


def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])


if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
    exit(0)