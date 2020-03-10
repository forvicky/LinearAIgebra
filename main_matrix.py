from playLA.Matrix import Matrix
from playLA.Vector import Vector

if __name__ == "__main__":  # 作为模块被导入时，不希望执行的代码
    matrix = Matrix([[1, 2], [3, 4]])
    print(matrix)
    print("matrix.shape()={}".format(matrix.shape()))
    print("matrix.size()={}".format(matrix.size()))
    print("len(matrix)={}".format(len(matrix)))
    print("matrix[0][0]={}".format(matrix[0, 0]))

    matrix2 = Matrix([[5, 6], [7, 8]])

    print("add:{}".format(matrix + matrix2))
    print("subtract:{}".format(matrix - matrix2))
    print("mul:{}".format(matrix * 2))

    print("zero_2_3:{}".format(Matrix.zero(2, 3)))

    vector = Vector([5, 6])
    print("{}*{}={}".format(matrix, vector, matrix.dot(vector)))

    print("{}*{}={}".format(matrix, matrix2, matrix.dot(matrix2)))
    print("{}*{}={}".format(matrix2, matrix, matrix2.dot(matrix)))

    print("matrix2.T={}".format(matrix2.T()))

    I = Matrix.identity(2)
    print(I)

    print("matrix2.dot(I)={}".format(matrix2.dot(I)))
    print("I.dot(matrix2)={}".format(I.dot(matrix2)))
