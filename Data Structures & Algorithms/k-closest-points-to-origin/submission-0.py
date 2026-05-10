class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distancetoorigin = defaultdict(list)

        for cord in points:
            distance = math.sqrt((0 -cord[0])**2 + (0 - cord[1])**2)
            distancetoorigin[distance].append(cord)
        distance_list = list(distancetoorigin.keys())
        heapq.heapify(distance_list)
        print(distancetoorigin)

        res = []

        while len(res) < k:
            value = heapq.heappop(distance_list)
            res.extend(distancetoorigin[value])
        return res






        