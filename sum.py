"""
Docstring for sum
"""


class Solution:
    def sumF(self, numbers: List[int], target: int):

        left, right = 0, len(numbers)-1
        total = 0


        for i in range(len(numbers)):
            total = numbers[left] + numbers[right]

            if target == total:
                return [left+1,right+1]
            
            elif target < numbers[i]:
                left+=1

            else:
                right+=1