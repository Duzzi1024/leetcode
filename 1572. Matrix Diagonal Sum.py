
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sum = 0
        for i in range(n) :
            sum += mat[i][i] + mat[i][n - i - 1]
        if n % 2 :
            w = n // 2
            sum -= mat[w][w]
        return sum