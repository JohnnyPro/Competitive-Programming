class Solution:
    def isArithmetic(self, array):
        array.sort()
        print(array)
        difference = array[1] - array[0]
        for i in range(2,len(array)):
            if array[i] - array[i-1] != difference: return False
        
        return True

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for i in range(len(l)):
            answer.append(self.isArithmetic(nums[l[i]:r[i]+1]))

        return answer
