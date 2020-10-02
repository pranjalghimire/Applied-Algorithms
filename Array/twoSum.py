"""
Two Sum
Name: Pranjal Ghimire
Language: Python
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=dict()
        for i in range(len(nums)):
            if target-nums[i] in a:
                return [a[target-nums[i]],i]
            else:
                a[nums[i]]=i
