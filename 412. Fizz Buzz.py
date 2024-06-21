class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        retData =[]
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 != 0:
                retData.append("Fizz")
            elif i % 3 != 0 and i % 5 == 0:
                retData.append("Buzz")
            elif i%3 == 0 and i%5 == 0:
                retData.append("FizzBuzz")
            else:
                retData.append(str(i))
        return retData