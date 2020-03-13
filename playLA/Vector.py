import math
from ._global import is_zero


class Vector:

    def __init__(self, lst):
        self._values = list(lst)  # 复制lst,防止引用调用被外部修改_values

    @classmethod  # 标示这个方法是类方法
    def zero(cls, dim):
        return cls([0] * dim)

    def norm(self):
        """返回向量的模"""
        return math.sqrt(sum(e ** 2 for e in self))

    def normalize(self):
        """返回向量的单位向量"""
        if is_zero(self.norm()):  # 浮点数判断不能用==0
            raise ZeroDivisionError("Normalize error! norm is zero.")

        return Vector(self._values) / self.norm()

    def __add__(self, other):
        assert len(self) == len(other), \
            "Error in adding.Length of vectors must be same."
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        assert len(self) == len(other), \
            "Error in subtracting.Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, other)])

    def underlying_list(self):
        """返回向量的底层列表"""
        return self._values[:]  # [:]表示返回列表的副本

    def dot(self, another):
        """向量点乘，返回结果标量"""
        assert len(self) == len(another), \
            "Error in dot product.Length of vectors must be same."

        return sum(a * b for a, b in zip(self, another))

    def __mul__(self, k):
        """返回self*k"""
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        """返回k*self"""
        return self * k

    def __truediv__(self, k):
        """返回数量除法的结果向量：self/k"""
        return (1 / k) * self

    def __pos__(self):
        """返回向量取正的结果向量"""
        return 1 * self

    def __neg__(self):
        """返回向量取负的结果向量"""
        return -1 * self

    def __iter__(self):
        """返回向量的迭代器"""
        return self._values.__iter__()

    def __len__(self):
        """ 返回向量维度 """
        return len(self._values)

    def __getitem__(self, index):
        """返回向量的第index个元素"""
        return self._values[index]

    # 供系统调用
    def __repr__(self):
        return "Vector({})".format(self._values)

    # 供用户手动调用,print()
    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))
