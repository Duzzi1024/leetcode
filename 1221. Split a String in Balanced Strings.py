class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_L = 0
        count_R = 0
        count = 0
        for i in s:
            if i == 'L':
                count_L += 1
            else:
                count_R += 1
            if (count_L == count_R):
                count += 1  
        return count