class Solution:

    def checkSorted(self, arr: List[int]) -> bool:
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True

    def panFlip(self, arr, k):
        if k == 1: return arr
        newArr = []
        for i in range(k-1, -1, -1):
            newArr.append(arr[i])
        
        newArr += arr[k:]
        return newArr 

    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        kArr = []
        n = len(arr)
        while not self.checkSorted(arr):
            maxIdx = arr.index(max(arr[:n]))
            if maxIdx != 0: 
                arr = self.panFlip(arr, maxIdx+1)
                kArr.append(maxIdx+1)
            arr = self.panFlip(arr, n)
            kArr.append(n)
            n -= 1


        return kArr
