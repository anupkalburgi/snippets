def rotate(matrix):
    rlen = len(matrix)
    clen = len(matrix[0])

    newMatrix = [["" for _ in range(clen)] for _ in range(rlen)]
    col = clen

    for r in range(rlen):
        col = col-1
        for c in range(clen):
            newMatrix[c][col] = matrix[r][c]
    return newMatrix


A = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g","h",  "i"]
]

print(rotate(A))