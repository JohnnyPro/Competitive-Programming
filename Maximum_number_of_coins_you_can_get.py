class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sum = 0
        idx = len(piles)-2
        for i in range(len(piles) // 3):
            sum += piles[idx]
            idx -= 2

        return sum
