class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dict_hn = {h: n for h, n in zip(heights, names)}
        heights.sort(reverse=True)
        return [dict_hn[h] for h in heights]