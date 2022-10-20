class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: continue
                if nums[j] < nums[i]: result[i] += 1

        return result
