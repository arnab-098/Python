import heapq
from typing import List


class Solution:
    def valid(self, i: int, j: int) -> bool:
        return i >= 0 and j >= 0 and i < self.ROW and j < self.COL

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        self.ROW: int = len(grid)
        self.COL: int = len(grid[0])

        directions: List[List[int]] = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        heap: List[tuple] = [(0, 0, 0)]

        while heap:
            obstacle, x, y = heapq.heappop(heap)

            if x == self.ROW - 1 and y == self.COL - 1:
                return obstacle

            for dx, dy in directions:
                nx: int = x + dx
                ny: int = y + dy
                if not self.valid(nx, ny) or (nx, ny) in visited:
                    continue
                visited.add((nx, ny))
                if grid[nx][ny] == 1:
                    heapq.heappush(heap, (obstacle + 1, nx, ny))
                else:
                    heapq.heappush(heap, (obstacle, nx, ny))

        return -1


def main() -> None:
    grid: List[List[int]] = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]
    x: Solution = Solution()
    result: int = x.minimumObstacles(grid)
    if result == -1:
        print("ERROR")
    else:
        print(result)


if __name__ == "__main__":
    main()
