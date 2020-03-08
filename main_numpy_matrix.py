import numpy as np

if __name__ == "__main__":
    # 矩阵的创建 numpy中矩阵和向量是同一个类
    A = np.array([[1, 2], [3, 4]])

    # 矩阵的属性
    print(A.shape)
    print(A.T)

    # 获取矩阵的元素
    print(A[1, 1])
    print(A[0])
    print(A[:, 0])  # :表示切片从0到最后

    # 矩阵的基本运算
    B = np.array([[5, 6], [7, 8]])
    print(A + B)
    print(A - B)
    print(10 * A)
    print(A * B)  # 在线性代数中无意义
    print(A.dot(B))  # 这个才是真正的矩阵乘法

    p = np.array([10, 100])
    print(A + p)  # 在线性代数中无意义
    print(A + 1)  # numpy中的广播

    print(A.dot(p))
