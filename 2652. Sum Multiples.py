class Solution:
    def sumOfMultiples(self, n: int) -> int:
        list1 = [i for i in range(1,n+1)]
        sum = 0
        for j in list1:
            if j%3 == 0 or j%5==0 or j%7==0:
                sum += j
        return sum