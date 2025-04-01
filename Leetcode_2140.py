from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        def rec(i: int) -> int:
            if i >= size:
                return 0
            if dp[i] != -1:
                return dp[i]

            point, brainpower = questions[i]
            take = point + rec(i + brainpower + 1)
            dont_take = rec(i + 1)

            dp[i] = max(take, dont_take)
            return dp[i]

        size = len(questions)
        dp = [-1] * size
        return rec(0)


if __name__ == "__main__":
    questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
    x = Solution()
    print(x.mostPoints(questions))
