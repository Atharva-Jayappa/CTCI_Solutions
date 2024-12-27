def zero(matrix) -> list[list]:
    z = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                z.append((row, col))

    rows = set()
    cols = set()

    for first, second in z:
        rows.add(first)
        cols.add(second)

    for i in rows:
        matrix[i] = [0] * len(matrix[i])

    for i in cols:
        for j in range(len(matrix)):
            matrix[j][i] = 0

    return matrix


def print_matrix(matrix):
    for row in matrix:
        for i in row:
            print(f"{i:3}", end=" ")
        print("")


if __name__ == "__main__":
    m = [[5, 9, 93, 0, 25],
         [5, 73, 81, 50, 22],
         [0, 15, 34, 0, 57],
         [67, 43, 33, 36, 1]]

    m1 = zero(m)
    print_matrix(m)

    #TODO Optimize Space complexity to O(1) currently O(R*C)
