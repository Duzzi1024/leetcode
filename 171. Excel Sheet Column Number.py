class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        c=0
        for i in columnTitle:
            c=c*26+(ord(i)-65)+1
        return c