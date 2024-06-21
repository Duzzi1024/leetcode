class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        whole = n // 7
        remainder = n % 7
        for i in range(whole):
          total = total + 7 * i + 28
        for i in range(remainder):
          total = total + whole + i + 1
        return total