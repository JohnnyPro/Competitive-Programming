class Solution(object):
    def calcSquareDist(self, point):
        """returns the square distance of any point from the origin"""
        return point[0] ** 2 + point[1]** 2

    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        minPts = points[:k]
        distances = [self.calcSquareDist(i) for i in minPts]
        maxDist = max(distances)

        for point in points[k:]:
            distance = self.calcSquareDist(point)
            if distance < maxDist:
                index = distances.index(maxDist)
                print(index)
                minPts[index] = point
                distances[index] = distance
                maxDist = max(distances)


        return minPts
