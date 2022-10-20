class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        sentence = s.split()
        sortedSentence = ['']*9
        for word in sentence:
            sortedSentence[int(word[-1])-1] = word[:-1]
        
        return ' '.join(sortedSentence).strip()
