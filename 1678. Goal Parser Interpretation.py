class Solution:
    def interpret(self, command: str) -> str:
        a = ""
        for i in command:
            a = a + i
        return(a.replace("()","o").replace("(al)","al"))