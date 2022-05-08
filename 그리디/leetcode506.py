class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        # max heap -> greedy alorithm에서 heap 사용빈도 높다
        heap = []
        for p in people:
            heapq.heappush(heap, (-p[0], p[1]))

        result = []
        while heap:
            p = heapq.heappop(heap)
            result.insert(p[1], [-p[0], p[1]])

        return result
