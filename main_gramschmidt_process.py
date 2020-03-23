from playLA.Vector import Vector
from playLA.GramSchmidtProcess import gram_schmidt_process

if __name__ == "__main__":
    basis1 = [Vector([2, 1]), Vector([1, 1])]
    res1 = gram_schmidt_process(basis1)
    for row in res1:
        print(row)

    res1 = [row/row.norm() for row in res1]
    for row in res1:
        print(row)
    print(res1[0].dot(res1[1]))