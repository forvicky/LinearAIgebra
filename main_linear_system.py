from playLA.Matrix import Matrix
from playLA.Vector import Vector
from playLA.LinearSystem import LinearSystem

if __name__ == "__main__":
    A = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    b = Vector([7, -11, 1])
    ls = LinearSystem(A, b)
    ls.gauss_jordan_elimination()
    ls.fancy_print()

    # 计算机浮点运算会有误差
    A2 = Matrix([[6, -3, 2], [5, 1, 12], [8, 5, 1]])
    b2 = Vector([31, 36, 11])
    ls2 = LinearSystem(A2, b2)
    ls2.gauss_jordan_elimination()
    ls2.fancy_print()
