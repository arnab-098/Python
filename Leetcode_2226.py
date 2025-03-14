from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        if k > total:
            return 0
        elif k == total:
            return 1
        left, right = 1, sum(candies) // k
        result = 0
        while left <= right:
            mid = (left + right) // 2
            count = 0
            for candy in candies:
                if candy < mid:
                    continue
                count += candy // mid
                if count >= k:
                    break
            if count >= k:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result


if __name__ == "__main__":
    x = Solution()
    print(x.maximumCandies([9, 10, 1, 2, 10, 9, 9, 10, 2, 2], 3))
