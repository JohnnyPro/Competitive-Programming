class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = start
        while end < len(nums):
            while start < len(nums) and nums[start] != 0:
                start += 1
            
            end = start
            while end < len(nums) and nums[end] == 0:
                end += 1
            
            if max(start, end) >= len(nums):
                break
                
            nums[start], nums[end] = nums[end], nums[start] 
        