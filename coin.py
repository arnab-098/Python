class Solution:
    def findMin(self, amount: int) -> int:
        count = 0
        max_coin = 1
        while amount > 0:
            amount -= max_coin
            max_coin *= 2
            count += 1
        return count


x = Solution()
n = int(input())
result = []
for i in range(n):
    amount = int(input())
    result.append(x.findMin(amount))
for i in result:
    print(i)
