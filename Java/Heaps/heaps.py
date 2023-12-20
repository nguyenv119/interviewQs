import heapq
from typing import List

class Soln:
    def test(self):
        assert self.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
        assert self.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
        assert self.findKthLargest([1], 1) == 1

        print("All Tests Passed")
    

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap) # O(k)
        
        for i in range(k, len(nums)): # (n - k)logk
            if nums[i] > heap[0]:
                heapq.heapreplace(heap, nums[i])

        return heap[0] 

Soln = Soln()
Soln.test()