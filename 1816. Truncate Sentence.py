class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        list1 = s.split(" ")
        list2 = list1[:k]
        result = " ".join(list2)
        return result