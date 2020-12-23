grid = [
        [1,  2,  3,  4], 
        [12, 13, 14, 5], 
        [11, 16, 15, 6], 
        [10, 9,  8,  7]
]
def pprint(row, col):
    print(grid[row][col])
n = 3 # n+1
for i in range(2):
    row = i
    for col in range(i, n-i):
        pprint(row, col)
    col = n-i
    for row in range(i, n-i):
        pprint(row, col)
    row = n-i
    for col in range(n-i, i, -1): # check
        pprint(row, col)
    col = i
    for row in range(n-i, i, -1):
        pprint(row, col)


def spiral(grid):
    result = []
    startRow, endRow = 0, len(grid)-1
    startCol, endCol = 0, len(grid[0])-1

    while startRow <= endRow and startCol  <= endCol:
        for col in range(startCol, endCol+1):
            result.append(grid[startRow][col])
        for row in range(startRow+1, endRow+1):
            result.append(grid[row][endCol])
        for col in range(endCol-1, startCol, -1):
            result.append(grid[endRow][col])
        for row in range(endRow, startRow, -1):
            result.append(grid[row][startCol])
        startRow = startRow + 1
        startCol = startCol + 1
        endCol = endCol - 1
        endRow = endRow - 1
    return result
print(spiral(grid))