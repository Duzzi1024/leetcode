class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c=int(a,2)
        d=int(b,2)
        e=c+d
        f=bin(e)
        return(f[2:])