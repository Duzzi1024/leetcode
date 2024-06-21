class Solution:
    def countEven(self, num: int) -> int:
        if num == 1 :
            return 0
        c = 0
        for i in range(2, num+1) :
            if sum(list(map(int, list(str(i))))) % 2 :
                continue
            c += 1
        return c