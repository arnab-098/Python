import heapq
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        k = n // 3

        leftMin = [0] * n
        rightMax = [0] * n

        maxHeap = []
        minHeap = []
        leftSum = rightSum = 0

        for i in range(n):
            heapq.heappush(maxHeap, -nums[i])
            leftSum += nums[i]
            if len(maxHeap) > k:
                leftSum += heapq.heappop(maxHeap)
            if i >= k - 1:
                leftMin[i] = leftSum

        for i in range(n - 1, -1, -1):
            heapq.heappush(minHeap, nums[i])
            rightSum += nums[i]
            if len(minHeap) > k:
                rightSum -= heapq.heappop(minHeap)
            if i <= n - k:
                rightMax[i] = rightSum

        result = float("inf")
        for i in range(k - 1, n - k):
            result = min(result, leftMin[i] - rightMax[i + 1])
        return int(result)
