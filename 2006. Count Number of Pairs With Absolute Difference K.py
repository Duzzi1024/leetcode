import numpy as np

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        A = np.array(nums).reshape((-1,1)) #(n,1)
        B = np.array(nums).reshape((1,-1)) #(1,n)
        C = np.abs(A-B) #(n,n)
        out = np.sum(C == k)
        return out//2