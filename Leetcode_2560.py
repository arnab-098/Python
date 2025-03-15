from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def isValid(capability):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= capability:
                    count += 1
                    if count == k:
                        break
                    i += 2
                else:
                    i += 1
            return count == k

        left, right = 1, max(nums)
        res = 0
        while left <= right:
            mid = (left + right) // 2
            if isValid(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res


if __name__ == "__main__":
    x = Solution()
    nums = [2, 3, 5, 9]
    k = 2
    print(x.minCapability(nums, k))
