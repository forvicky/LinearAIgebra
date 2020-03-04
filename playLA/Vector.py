class Vector:

    def __init__(self, lst):
        self._values = list(lst)  # 复制lst,防止引用调用被外部修改_values

    def __add__(self, other):
        assert len(self) == len(other), \
            "Error in adding.Length of vectors must be same."
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        assert len(self) == len(other), \
            "Error in subtracting.Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, other)])

    def __mul__(self, k):
        """返回self*k"""
        return Vector([k*e for e in self])

    def __rmul__(self, k):
        """返回k*self"""
        return self*k

    def __pos__(self):
        """返回向量取正的结果向量"""
        return 1*self

    def __neg__(self):
        """返回向量取负的结果向量"""
        return -1*self

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
