"""
Docstring for rob
"""


class Solution:

    def rob(self, nums:List[int]):

        prev2, prev1 = 0, 0


        for amount in nums:
            current = max(prev1, amount+prev2)
            prev2 = prev1
            prev1 = current


        return prev1

        

