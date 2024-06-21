class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        list1 = []
        for i in accounts:
            list1.append(sum(i))
        return max(list1)