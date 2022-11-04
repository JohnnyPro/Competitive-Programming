class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        lowerHalf = []
        upperHalf = []
        count = 0
        for i in nums:
            
            if i >= k: continue # since we are only interested in numbers lower than k
            if i < k/2:
                lowerHalf.append(i)
            elif i == k/2:
                count += 0.5
            else:
                upperHalf.append(i)

        upperHalf.sort()
        for i in lowerHalf:
            if k-i in upperHalf:
                count += 1
                upperHalf.remove(k-i)
        
        return int(count)
