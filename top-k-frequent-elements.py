class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # countingMap to count
        # filter by value (> k)
        # return keys

        countingMap = dict.fromkeys(nums, 0)
        for number in nums:
            countingMap[number] += 1 
        
        result = []
        result = sorted(countingMap.items(), key=lambda x:x[1], reverse=True)[:k]
        result = [item[0] for item in result]
        return result
