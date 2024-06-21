class Solution:
    def maxDepth(self, s: str) -> int:
        leftCount = 0
        maxDepth = 0
        for c in s:
            match c:
                case "(":
                    leftCount += 1
                case ")":
                    leftCount -= 1
            maxDepth = max(leftCount, maxDepth)
        return maxDepth