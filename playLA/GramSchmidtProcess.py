from .Vector import Vector
from .Matrix import Matrix
from .LinearSystem import rank


def gram_schmidt_process(basis):
    matrix = Matrix(basis)
    assert rank(matrix) == len(basis) # 保证所有向量线性无关

    res = [basis[0]]
    for i in range(1,len(basis)):
        p = basis[i]
        for r in res:
            p = p-basis[i].dot(r) / r.dot(r) * r
