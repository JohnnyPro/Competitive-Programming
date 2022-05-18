class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        newNum = ''
        targetlength = len(num) - k
        
        if targetlength > 0:
            if max(num[:len(num)-k]) == min(num[:len(num)-k]):
                if max(num[:len(num)-k]) <= min(num):
                    return str(int(num[:len(num)-k]))
        

        while k > 0:
            if len(newNum) == targetlength:
                num = ''
                break
            temp = min(num[:k+1])
            i = num.index(temp)
            num = num[i+1:]
            newNum += temp
            k -= i
        
        newNum += num
        
        if newNum == '':
            newNum = '0'
        return str(int(newNum))
