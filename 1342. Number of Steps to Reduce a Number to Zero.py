class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num !=0:
            if num % 2 ==0 :
                count = count+1
                num = num/2
            else :
                count = count +1
                num = num-1
        return count