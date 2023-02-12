threshold = 1e-8


def isZero(val):
    return abs(val) < threshold


def isNotZero(val):
    return abs(val) >= threshold


def greaterZero(val):
    return val > threshold


def greaterEqualZero(val):
    return val >= threshold


def smallerZero(val):
    return val < -threshold


def smallerEqualZero(val):
    return val <= -threshold


def printMatrix(matrix):
    # Find the maximum length of an element in each column
    max_lengths = [0] * len(matrix[0])
    for row in matrix:
        for i, item in enumerate(row):
            max_lengths[i] = max(max_lengths[i], len(str(item)))

    # Build the format string for each column
    format_string = " ".join("{{:>{}}}".format(length) for length in max_lengths)

    # Print each row using the format string
    for row in matrix:
        print(format_string.format(*row))


def dotProduct(A, B):
    if len(A) != len(B):
        raise Exception("Dot product for unequal size vectors")
    dotSum = 0
    for i in range(len(A)):
        dotSum += A[i] * B[i]
    return dotSum


# Converts given AX<=b to AX+y=b I.e. adds alick/slack variables
def preProcess(A, b, c, m, n):
    newN = m + n
    newA = [[None for j in range(newN)] for i in range(m)]
    for i in range(m):
        if greaterEqualZero(b[i]):
            for j in range(n):
                newA[i][j] = A[i][j]
            for j in range(n, newN):
                if j - n == i:
                    newA[i][j] = 1
                else:
                    newA[i][j] = 0
        else:
            for j in range(n):
                newA[i][j] = -A[i][j]
            for j in range(n, newN):
                if j - n == i:
                    newA[i][j] = -1
                else:
                    newA[i][j] = 0
            b[i] = -b[i]
        c.append(0)
    return newA, b, c, m, newN


#   Problem must be in the form of AX=b
class Simplex2Phase:
    def __init__(self, A, b, c, m, n):
        self.auxC = None
        self.b = b
        self.c = c
        self.m = m
        self.n = n
        self.mm = m + 1  # Num rows
        self.nn = n + m + 1  # Num columns
        self.initializeTable(A)
        self.solIndex = [i for i in range(n + 1, self.nn)]

    # Adds articifical variables and initializes the table
    def initializeTable(self, A):
        table = [[None for j in range(self.nn)] for i in range(self.mm)]
        for i in range(self.mm):
            for j in range(self.nn):
                val = None
                if i == 0:
                    if j == 0:
                        val = 0
                    elif j <= self.n:
                        val = self.c[j - 1]
                    else:
                        val = 0
                else:
                    if j == 0:
                        val = self.b[i - 1]
                    elif j <= self.n:
                        val = A[i - 1][j - 1]
                    elif i - 1 == j - self.n - 1:
                        val = 1
                    else:
                        val = 0
                if val is None:
                    raise Exception("Invalid None found in table")
                table[i][j] = val
        self.table = table
        # self.auxC = [1 for i in range(self.m)]
        # for i in range(self.n + 1):
        #     col = [None for j in range(self.m)]
        #     for j in range(self.m):
        #         col[j] = table[j + 1][i]
        #     table[0][i] = -dotProduct(col, self.auxC)
        # return table

    # Sets the reduced costs of the upper row by using -cBA[i]
    def phase1Initialize(self):
        self.auxC = [1 for i in range(self.m)]
        for i in range(self.n + 1):
            col = [None for j in range(self.m)]
            for j in range(self.m):
                col[j] = self.table[j + 1][i]
            self.table[0][i] = -dotProduct(col, self.auxC)

    # Returns the largest negative number. If all are non negative returns 0
    def getPivotColumn(self):
        negMin = -float('inf')
        negMinIndex = -1
        for i in range(1, self.nn):
            if smallerZero(self.table[0][i]) and self.table[0][i] > negMin:
                negMin = self.table[0][i]
                negMinIndex = i
        return negMinIndex

    # Returns the row index that has the largest negative number. If no negative numbers then returns -1
    def getPivotRow(self, pivotColumn):
        minRatio = float('inf')
        minRatioIndex = -1
        for i in range(1, self.mm):
            if greaterZero(self.table[i][pivotColumn]):
                r = self.table[i][0] / self.table[i][pivotColumn]
                # if r<0:
                #     raise Exception("Negative solution for basis variable")
                if r < minRatio:
                    minRatio = r
                    minRatioIndex = i
        return minRatioIndex

    # Normalizes the given row using pivot element
    def normalizePivotRow(self, pivotRow, pivotColumn):
        divValue = self.table[pivotRow][pivotColumn]
        for i in range(self.nn):
            self.table[pivotRow][i] /= divValue

    # Make pivotColumn element in row 0 by using row operations
    def rowOperation(self, pivotRow, pivotColumn, row):
        if pivotRow == row:
            return
        mulValue = self.table[row][pivotColumn]
        for i in range(self.nn):
            self.table[row][i] -= mulValue * self.table[pivotRow][i]

    # Makes all the other elements in pivot column0 except the pivot element
    def carryRowOperations(self, pivotRow, pivotColumn):
        for i in range(self.mm):
            if i != pivotRow:
                self.rowOperation(pivotRow, pivotColumn, i)

    # Exist spivotRow-1 vector and enters pivotColumn vector into basis
    def setBasis(self, pivotRow, pivotColumn):
        self.solIndex[pivotRow - 1] = pivotColumn

    # Gets the first non zero column in given artificial basic row. If such column does not
    # exist returns -1
    def getPivotColumnForArtificialBasic(self, row):
        for i in range(1, self.n + 1):
            if isNotZero(self.table[row][i]):
                return i
        return -1

    # Removes the given redundant row
    def removeRedundantRow(self, row):
        self.table.pop(row)
        self.solIndex.pop(row - 1)
        self.m -= 1
        self.mm -= 1

    # Replaces / Removes all artificial variables from the basis
    def removeArtificialBasic(self):
        i = 0
        while i < self.m:
            if self.solIndex[i] > self.n:
                pivotRow = i + 1
                pivotColumn = self.getPivotColumnForArtificialBasic(pivotRow)
                if pivotColumn == -1:
                    i -= 1
                    self.removeRedundantRow(pivotRow)
                else:
                    self.normalizePivotRow(pivotRow, pivotColumn)
                    self.carryRowOperations(pivotRow, pivotColumn)
                    self.setBasis(pivotRow, pivotColumn)
            i += 1

    # Removes artificial columns
    def removeArtificialColumns(self):
        for i in range(self.mm):
            self.table[i] = self.table[i][:self.n + 1]
        self.nn = self.n + 1

    # Removes artificial variables after the phase 1
    def phase1PostProcess(self):
        self.removeArtificialBasic()
        self.removeArtificialColumns()

    # Uses the simplex method to solve the tableU. Also detects infeasible or infinity
    def simplex(self, phase):
        while 1:
            pivotColumn = self.getPivotColumn()
            if pivotColumn == -1:
                if phase == 1:
                    # Infeasibility
                    if isNotZero(self.table[0][0]):
                        return -1
                    return 0
                elif phase == 2:
                    return self.getSolution()
            pivotRow = self.getPivotRow(pivotColumn)
            # Infinity
            if pivotRow == -1:
                return 1
            self.normalizePivotRow(pivotRow, pivotColumn)
            self.carryRowOperations(pivotRow, pivotColumn)
            self.setBasis(pivotRow, pivotColumn)

    # Sets reduced costs to the upper row of phase 2 tableU
    def phase2Initialize(self):
        colProductSum = 0
        for j in range(self.m):
            colProductSum += self.c[self.solIndex[j] - 1] * self.table[j + 1][0]
        self.table[0][0] = -colProductSum
        costVector = [self.c[i - 1] for i in self.solIndex]
        cBBA = []
        for i in range(self.n):
            col = [None for j in range(self.m)]
            for j in range(self.m):
                col[j] = self.table[j + 1][i + 1]
            cBBA.append(dotProduct(col, costVector))
        upperRow = [self.c[i] - cBBA[i] for i in range(self.n)]
        self.table[0] = [self.table[0][0]] + upperRow

    # Gets solutions for original variables provided to object
    def getSolution(self):
        rowSol = [self.table[i][0] for i in range(1, self.mm)]
        processedSol = [0 for i in range(self.n)]
        for i in range(self.m):
            processedSol[self.solIndex[i] - 1] = rowSol[i]
        return processedSol


# Removes slack/slick variables
def postProcess(sols, initialN):
    return sols[:initialN]


#   n   =   Number of variables
#   m   =   Number of inequalities
#   c   =   Optimization objective
#   Problem must be in the form of AX<=b
#   minMax = min if optimization is minimum max otherwise
def solve_LP(n, m, A, b, c, minMax):
    if minMax == "max":
        c = [-i for i in c]
    elif minMax != "min":
        raise Exception("Invalid minmax value")
    initialN = n
    A, b, c, m, n = preProcess(A, b, c, m, n)
    auxObj = Simplex2Phase(A, b, c, m, n)
    auxObj.phase1Initialize()
    condition = auxObj.simplex(1)
    if condition != 0:
        return condition, None
    auxObj.phase1PostProcess()
    auxObj.phase2Initialize()
    x = auxObj.simplex(2)
    if x == 1:
        return 1, None
    return 0, postProcess(auxObj.getSolution(), initialN)


filename = "./tests/a"
f = open(filename, "r")
M, N = list(map(int, f.readline().split()))
A = []
for i in range(M):
    A += [list(map(int, f.readline().split()))]
B = list(map(int, f.readline().split()))
C = list(map(int, f.readline().split()))
anst, ansx = solve_LP(N, M, A, B, C, "max")
if anst == -1:
    print("No solution")
if anst == 0:
    print("Bounded solution")
    print(' '.join(list(map(lambda x: '%.10f' % x, ansx))))
if anst == 1:
    print("Infinity")
