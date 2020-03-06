from playLA.Vector import Vector

class Matrix:

    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]

    def row_vector(self,index):
        """返回矩阵的第index个行向量"""
        return Vector(self._values[index])

    def col_vector(self,index):
        return Vector([row[index] for row in self._values])

    def __getitem__(self, pos):
        """返回矩阵pos位置的元素"""
        r, c = pos   # 元组
        return self._values[r][c]

    def size(self):
        """返回矩阵有多少个元素"""
        r, c = self.shape()
        return r * c

    def row_num(self):
        return self.shape()[0]

    def col_num(self):
        return self.shape()[1]

    def shape(self):
        """返回矩阵的形状：（行数，列数）"""
        return len(self._values), len(self._values[0])

    def __repr__(self):
        return "Matrix({})".format(self._values)

    __str__ = __repr__

    __len__ = row_num
