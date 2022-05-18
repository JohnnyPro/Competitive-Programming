class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        for i in range(k):
            for j in range(len(num)-1):
                if int(num[j]) > int(num[j+1]):
                    num = num[:j] + num[j+1:]
                    break
                if j == len(num)-2:
                    numToReplace = max(num)
                    num.replace(numToReplace, '0', 1)
        return str(int(num))
                    
                