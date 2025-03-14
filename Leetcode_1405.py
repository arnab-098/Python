import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []

        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, "a"))
        if b > 0:
            heapq.heappush(pq, (-b, "b"))
        if c > 0:
            heapq.heappush(pq, (-c, "c"))

        while pq:
            val1, char1 = heapq.heappop(pq)
            if len(res) >= 2 and res[-1] == char1 and res[-2] == char1:
                if not pq:
                    break
                val2, char2 = heapq.heappop(pq)
                res.append(char2)
                val2 += 1
                if val2 < 0:
                    heapq.heappush(pq, (val2, char2))
                heapq.heappush(pq, (val1, char1))
            else:
                res.append(char1)
                val1 += 1
                if val1 < 0:
                    heapq.heappush(pq, (val1, char1))

        return "".join(res)


if __name__ == "__main__":
    x = Solution()
    a = 7
    b = 1
    c = 0
    print(x.longestDiverseString(a, b, c))
