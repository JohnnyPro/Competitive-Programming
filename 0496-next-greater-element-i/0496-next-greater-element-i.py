class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsHash = {n:i for  i, n in enumerate(nums1)}
        res = [-1]*len(nums1)
        nextGreater = []
        nums2.reverse()
        stack = []
        for num in nums2:
            #find greater element
            while stack and stack[-1] <= num:
                stack.pop()
            
            if num in numsHash:
                if stack:
                    res[numsHash[num]] = stack[-1]
                else:
                    res[numsHash[num]] = -1
                
            stack.append(num)
            
        return res
            