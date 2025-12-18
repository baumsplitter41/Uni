
A = [[0, 0],
     [0, 0],
     [0, 0]]
B = [[0, 0],
     [0, 0]]


def matrix_input(A):
    for x in range(len(A)):
        for y in range(len(A[0])):
            a = input(f"Input number for A[{x}][{y}]: ")
            A[x][y] = int(a)
    print(A)


matrix_input(A)
matrix_input(B)



def matrix_multiplication(A,B):
     C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
     for i in range(len(A)):
          for j in range(len(B[0])):
               for k in range(len(B)):
                    C[i][j] += A[i][k] * B[k][j]
     return C
print(matrix_multiplication(A,B))

