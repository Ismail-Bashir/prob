"""
furthest you can jump game

"""

class Solution:
    def gmae(self, nums: List[int]):
        

        furthest = 0


        for i in range(len(nums)):
            if i > furthest:
                return False
            
            furthest = max(furthest, nums[i]+i)

            if furthest >= len(nums):
                return True

