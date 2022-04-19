# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]=max(nums[i],nums[i]+nums[i-1])
        return max(nums)