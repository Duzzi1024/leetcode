class Solution:
    def pivotInteger(self, n: int) -> int:
        i, j = 0, n
        sum_i, sum_j = 0, 0
        while i <= j:
            if sum_i < sum_j:
                sum_i += i
                i += 1
            else:
                sum_j += j
                j -= 1
        
        return i if sum_i + i == sum_j else -1