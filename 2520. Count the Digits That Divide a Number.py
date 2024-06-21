class Solution:
    def countDigits(self, num: int) -> int:
        count = 0 
        list1 = list(str(num))
        print(list1)
        for i in list1:
            if num% int(i) ==0:
                count += 1
        return count