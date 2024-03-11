# LC HARD
# Link: https://leetcode.com/problems/find-median-from-data-stream/discuss/4856480/Python-using-the-2-heap-algorithm-with-intuition-and-comments

import heapq
class MedianFinder:

    def __init__(self):
        # Using the Two Heaps Algorithm for finding the meadian of a data-stream
        # A max heap to maintain the lower half of the numbers. (so, the top of heap is closest to middle)
        # A min heap to maintain the upper half of the numbers. (so, the top of heap is closest to middle)
        self.min_heap = []
        heapq.heapify(self.min_heap)
        self.min_heap_size = 0
        
        self.max_heap = []
        heapq.heapify(self.max_heap)
        self.max_heap_size = 0

    def addNum(self, num: int) -> None:
        # Python only has min heap, so we use negative values for simulating a max heap
        if self.max_heap_size == 0 or num <= -1*self.max_heap[0]:
            heapq.heappush(self.max_heap, -1*num)
            self.max_heap_size += 1
        else:
            heapq.heappush(self.min_heap, num)
            self.min_heap_size += 1
            
        # Now we have to balance the heaps
        # so that an heap is not bigger than the other heap by more than 1 element
        # move an element from the larger heap to the smaller one.
        if self.max_heap_size - self.min_heap_size > 1:
            # pushing the biggest in max heap (lower half) to the min heap (upper half)
            heapq.heappush(self.min_heap, -1*heapq.heappop(self.max_heap))
            self.max_heap_size -= 1 
            self.min_heap_size += 1
        elif self.min_heap_size - self.max_heap_size > 0:
            # pushing the smallest in min heap (upper half) to the max heap (lower half)
            heapq.heappush(self.max_heap, -1*heapq.heappop(self.min_heap))
            self.max_heap_size += 1 
            self.min_heap_size -= 1
        
        # Note:
        # The reason for the difference in conditions is to maintain a balance between the two heaps 
        # while allowing for the total number of elements to be either odd or even. 
        # The goal is to ensure that if the total number of elements is odd, 
        # the max heap (which stores the smaller half of the numbers) contains one more element than the min heap (which stores the larger half). 
        # If the total number is even, both heaps should have the same number of elements.
        # And the median is the average of top element of the two heaps.

    def findMedian(self) -> float:
        # size of data stream is even
        if self.max_heap_size == self.min_heap_size:
            return (-1*self.max_heap[0] + self.min_heap[0]) / 2
        # size of data stream is odd
        else:
            return -1*self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
