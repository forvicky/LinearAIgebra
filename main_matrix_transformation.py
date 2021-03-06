import matplotlib.pyplot as plt   # 画图包
from playLA.Matrix import Matrix
from playLA.Vector import Vector
import math

if __name__ == "__main__":
    points = [[0, 0], [0, 5], [3, 5], [3, 4], [1, 4],
              [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]]

    x = [point[0] for point in points]
    y = [point[1] for point in points]

    # 窗口大小
    plt.figure(figsize=(5, 5))
    # x坐标
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    # 折线图
    plt.plot(x, y)
    # plt.show()

    P = Matrix(points)

    # T 就是变换矩阵，线性代数在图形学中的应用
    # T = Matrix([[2, 0], [0, 1.5]])
    # T = Matrix([[1, 0], [0, -1]])
    # T = Matrix([[-1, 0], [0, 1]])
    # T = Matrix([[-1, 0], [0, -1]])
    # T = Matrix([[1, 0.5], [0, 1]]) # x错切
    # T = Matrix([[1, 0], [0.5, 1]])   # y错切
    theta = math.pi / 3   # 角度 * math.pi /180 = 弧度   sin cos中使用的都是弧度
    T = Matrix([[math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)]])

    P2 = T.dot(P.T())
    plt.plot([P2.col_vector(i)[0] for i in range(P2.col_num())], [P2.col_vector(i)[1] for i in range(P2.col_num())])
    plt.show()
