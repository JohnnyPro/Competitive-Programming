class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        previous = -1
        for i in popped:
            pos  = pushed.index(i)
            
            if len(pushed) == 1:
                return True
            # Two cases
            # pos is higher than previous
            
            if pos > previous:
                pushed.pop(pos)
                previous = pos-1

                
            # pos is lower than previous
            else:
                if previous - pos == 0:
                    previous = pos-1
                    pushed.pop(pos)
                    continue
                
                else:
                    return False