class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        countingMap = [0]*100001
        for number in arr:
            countingMap[number] += 1
        
        countingMap.sort(key=None, reverse=True)
        i = 0
        sum = 0
        while sum < len(arr)/2:
            sum += countingMap[i]
            i +=1
        
        return i
