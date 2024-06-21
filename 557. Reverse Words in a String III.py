class Solution:
    def reverseWords(self, s: str) -> str:
        x=list(s.split())
        l=[]
        a=""
        for i in x:
            l.append(i[::-1]+" ")
        for i in l:
            a+=i
        return a[:len(a)-1]