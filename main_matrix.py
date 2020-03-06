from playLA.Matrix import Matrix

if __name__ == "__main__":  # 作为模块被导入时，不希望执行的代码
    matrix = Matrix([[1, 2], [3, 4]])
    print(matrix)
    print("matrix.shape()={}".format(matrix.shape()))
    print("matrix.size()={}".format(matrix.size()))
    print("len(matrix)={}".format(len(matrix)))
    print("matrix[0][0]={}".format(matrix[0,0]))
