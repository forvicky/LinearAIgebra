import numpy as np  # 别名

if __name__ == "__main__":
    print(np.__version__)

    lst = [1, 2, 3]
    lst[0] = "hello"
    print(lst)

    vec = np.array([1, 2, 3])  # 创建向量
    print(vec)
    # vec[0]="hello"
    # vec[0] = 66
    # print(vec)

    # np.array的创建
    print(np.zeros(5))
    print(np.ones(5))
    print(np.full(5, 666))

    # np.array的基本属性
    print(vec)
    print("size=", vec.size)
    print("size=", len(vec))
    print(vec[0])
    print(vec[-1])
    print(vec[0:2])

    # np.array的基本运算
    vec2 = np.array([4, 5, 6])
    print("{} + {}={}".format(vec, vec2, vec + vec2))
    print("{} - {}={}".format(vec, vec2, vec - vec2))
    print("{} * {}={}".format(2, vec2, 2 * vec2))
    print("{} * {}={}".format(vec, vec2, vec * vec2))  # 没有数学意义
    print("{}.dot({})={}".format(vec, vec2, vec.dot(vec2)))

    print(np.linalg.norm(vec))  # 求模
    print(vec / np.linalg.norm(vec))  # 单位向量
    print(np.linalg.norm(vec / np.linalg.norm(vec)))  # 单位向量

    zero3 = np.zeros(3)
    # zero3 / np.linalg.norm(zero3)