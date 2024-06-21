class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        tot=0
        while(1):
            if(mainTank>=5):
                tot+=5*10
                mainTank-=5
                if additionalTank>=1:
                    mainTank+=1
                    additionalTank-=1
            else:
                break
        tot+=mainTank*10
        return tot