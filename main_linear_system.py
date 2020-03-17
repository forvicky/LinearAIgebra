from playLA.Matrix import Matrix
from playLA.Vector import Vector
from playLA.LinearSystem import LinearSystem
from playLA.LinearSystem import inv

if __name__ == "__main__":
    A = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    b = Vector([7, -11, 1])
    ls = LinearSystem(A, b)
    ls.gauss_jordan_elimination()
    ls.fancy_print()

    print("")

    A2 = Matrix([[6, -3, 2], [5, 1, 12], [8, 5, 1]])
    b2 = Vector([31, 36, 11])
    ls2 = LinearSystem(A2, b2)
    ls2.gauss_jordan_elimination()
    ls2.fancy_print()

    print("")

    A3 = Matrix([[1, -1, 2, 0, 3],
                 [-1, 1, 0, 2, -5],
                 [1, -1, 4, 2, 4],
                 [-2, 2, -5, -1, -3]]
                )
    b3 = Vector([1, 5, 13, -1])
    ls3 = LinearSystem(A3, b3)
    ls3.gauss_jordan_elimination()
    ls3.fancy_print()

    print("")

    A4 = Matrix([[2, 2],
                 [2, 1],
                 [1, 2]]
                )
    b4 = Vector([3, 2.5, 7])
    ls4 = LinearSystem(A4, b4)
    print(ls4.gauss_jordan_elimination())
    ls4.fancy_print()

    A = Matrix([[1, 2], [3, 4]])
    invA = inv(A)
    print(invA)
    # 计算机浮点运算会有误差
    print(A.dot(invA))
    print(invA.dot(A))
