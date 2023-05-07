class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        
        stack = []
        tempHash = {}
        for i, n in enumerate(temperatures):
            if n in tempHash:
                tempHash[n].append(i)
            else:
                tempHash[n] = [i]
        print(tempHash)
        result = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1] < temp:
                val = stack.pop()
                idx = tempHash[val].pop(0)
                result[idx] = i - idx
            
            stack.append(temp)
            
        return result