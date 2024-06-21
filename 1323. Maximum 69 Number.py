class Solution:
    def maximum69Number (self, num: int) -> int:
        res=0
        val=list(str(num))
        for i in range(len(val)):
            temp=list(str(num))
            if val[i]=='6':
                temp[i]="9"
            i_temp=int("".join(temp))
            if i_temp>res:
                res=i_temp
        return res