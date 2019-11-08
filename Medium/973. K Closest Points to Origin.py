'''We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:
Input: points = [[1,3],[-2,2]], K = 1

Output: [[-2,2]]'''

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        heap = []
        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x , y))
            else:
                heapq.heappush(heap, (dict, x ,y))
        return [(x,y) for (dist, x, y) in heap]
