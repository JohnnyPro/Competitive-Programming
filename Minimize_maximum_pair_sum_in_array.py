class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maximum = nums[0] + nums[len(nums)-1]
        for i in range(len(nums) // 2):
            temp = nums[i] + nums[len(nums)-1-i]
            maximum = temp if temp > maximum else maximum
        
        return maximum
