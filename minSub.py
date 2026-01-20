"""
Docstring for minSub
"""


class Solution:

    def sub2(self, nums: List[int], target:int):
        left = 0
        total = 0
        minLen = float("inf")



        for i in range(len(nums)):
            total+=nums[i]
            while total >= target:
                total -= nums[i]
                minLen= min(minLen, i-left+1)
                left+=1


        return minLen if minLen!=float("inf") else 0