class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # count numbers smaller than target, and the number of times target occurs
        base, freq = 0, 0  
        
        for i in nums:
            if i < target:
                base +=1
            elif i == target:
                freq += 1

        return [i for i in range(base, base+freq)]
