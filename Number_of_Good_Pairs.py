class Solution:
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n-1)

    def Combination(self, n, r=2):
        return self.factorial(n) / (self.factorial(n-r) * self.factorial(r))
    
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numOfOccurences = []
        for i in range(101):
            numOfOccurences.append(nums.count(i))
        
        result = 0
        for i in numOfOccurences:
            if i > 1:
                result += self.Combination(i)

        return int(result)
