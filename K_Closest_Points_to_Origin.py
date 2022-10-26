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
        distList = []
        pointList = []
        result = []
        for point in points:
            distance = self.calcSquareDist(point)
            distList.append(distance)
            pointList.append(point)
        
        for i in range(k):
            smallIndex = distList.index(min(distList))
            result.append(pointList.pop(smallIndex))
            distList.pop(smallIndex)

        return result
