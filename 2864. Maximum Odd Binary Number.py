class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return '1'*((a := s.count('1'))-1)+'0'*(len(s)-a)+'1'