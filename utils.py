from typing import List
from math import sqrt
from pprint import pprint


class Vector:
    def __init__(self, vector: List[float]):
        self.__dimension = len(vector)
        self.__vector = vector[:]

    def to_list(self) -> List[float]:
        return self.__vector[:]

    def __len__(self):
        return self.__dimension

    def __add__(self, other):
        if isinstance(other, Vector) and other.__dimension == self.__dimension:
            return Vector([self[i] + other[i] for i in range(self.__dimension)])
        return NotImplemented  # Only two vectors with equal dimension could be added

    def __sub__(self, other):
        if isinstance(other, Vector) and other.__dimension == self.__dimension:
            return Vector([self[i] - other[i] for i in range(self.__dimension)])
        return NotImplemented  # Only two vectors with equal dimension could be subtracted

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.__vector[item]
        if isinstance(item, slice):
            return Vector([self.__vector[i] for i in range(slice.start, slice.stop, slice.step)])
        return NotImplemented  # Key should be either an integer or a slice object

    def __abs__(self):  # Euclidean norm with scaling to avoid underflow and overflow
        max_abs = abs(self.__vector[0])
        for i in range(self.__dimension):
            x = abs(self.__vector[i])
            if x > max_abs:
                max_abs = x
        if max_abs == 0:
            return 0
        scaled_sum = 0
        for i in range(self.__dimension):
            x = self.__vector[i] / max_abs
            scaled_sum += x * x
        return sqrt(scaled_sum) * max_abs

    def __mul__(self, other):
        if isinstance(other, Vector):
            return [
                [
                    self.__vector[i] * other[j] for j in range(other.__dimension)
                ] for i in range(self.__dimension)
            ]
        if isinstance(other, float):
            return self.scalar(other)
        return NotImplemented  # Only vectors and scalar values are supported as right operand

    def scalar(self, r: float):
        return Vector([self.__vector[i] * r for i in range(self.__dimension)])

    def __rmul__(self, other):
        if isinstance(other, float):
            return self.scalar(other)
        return NotImplemented  # Only scalar values are supported as left operand


class Matrix:
    def __init__(self, matrix: List[List[float]]):
        self.__dimension = len(matrix)
        self.__matrix = [matrix[i][:] for i in range(self.__dimension)]

    def __len__(self):
        return self.__dimension

    def cell(self, i: int, j: int):
        return self.__matrix[i][j]

    def __sub__(self, other):
        if isinstance(other, Matrix) and self.__dimension == other.__dimension:
            return Matrix([
                [
                    self.__matrix[i][j] - other.cell(i, j) for j in range(self.__dimension)
                ] for i in range(self.__dimension)
            ])
        return NotImplemented  # Only two matrices with equal dimension could be subtracted

    def column(self, i: int) -> Vector:
        return Vector([self.__matrix[j][i] for j in range(self.__dimension)])

    def pretty_print(self):
        pprint(self.__matrix)

    def __mul__(self, other):
        if isinstance(other, Vector):
            result = [0] * self.__dimension
            for i in range(self.__dimension):
                for j in range(self.__dimension):
                    result[i] += self.__matrix[i][j] * other[j]
            return Vector(result)
        return NotImplemented  # Only vectors with the same dimension as the matrix are supported as right operand

    def __rmul__(self, other):
        if isinstance(other, Vector):
            result = [0] * self.__dimension
            for i in range(self.__dimension):
                for j in range(self.__dimension):
                    result[i] += self.__matrix[j][i] * other[j]
            return Vector(result)
        return NotImplemented  # Only vectors with the same dimension as the matrix are supported as left operand

    @classmethod
    def identity(cls, n: int):
        return cls([[1 if i == j else 0 for j in range(n)] for i in range(n)])


def to_upper_hessenberg(A: List[List[float]]) -> (Matrix, Matrix):  # O(n^3) algorithm
    n = len(A)
    B = Matrix(A)
    Q = Matrix.identity(n)
    for i in range(n - 2):
        column = B.column(i).to_list()
        x = Vector([0.0] * (i + 1) + column[i + 1:])
        y = Vector([0.0] * (i + 1) + [abs(x)] + [0.0] * (n - i - 2))
        u = x - y
        norm_u = abs(u)
        if norm_u == 0:
            continue
        gamma = 2 / (norm_u * norm_u)
        # Q_i = I - gamma * u * u^T
        C = B - Matrix((B * u) * (gamma * u))  # C = B * Q_i
        B = C - Matrix((gamma * u) * (u * C))  # B = Q_i * C
        Q = Q - Matrix((Q * u) * (gamma * u))  # Q = Q * Q_i
    return B, Q


if __name__ == "__main__":
    A = [
        [3, 2, 4],
        [0, 5, 6],
        [4, 7, 3]
    ]
    B, Q = to_upper_hessenberg(A)
    B.pretty_print()
    Q.pretty_print()
