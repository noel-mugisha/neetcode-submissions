class MedianFinder:

    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.left_max_heap, num)

        if self.right_min_heap and self.left_max_heap[0] > self.right_min_heap[0]:
            right_val = heapq.heappop(self.right_min_heap)
            left_val = heapq.heappop_max(self.left_max_heap)

            heapq.heappush_max(self.left_max_heap, right_val)
            heapq.heappush(self.right_min_heap, left_val)

        if len(self.left_max_heap) - len(self.right_min_heap) > 1:
            val = heapq.heappop_max(self.left_max_heap)
            heapq.heappush(self.right_min_heap, val)
        

    def findMedian(self) -> float:
        if len(self.left_max_heap) == len(self.right_min_heap):
            return (self.left_max_heap[0] + self.right_min_heap[0]) / 2
        return self.left_max_heap[0]
        
        