class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        list1 = [int(i) for i in str(n)]
        a= 1
        b = 0
        for j in list1:
            a *= j
            b += j
        return a-b