from typing import List
import heapq


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        ROW: int = len(grid)
        COL: int = len(grid[0])

        directions: List[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        heap: List[tuple[int, int, int]] = [(0, 0, 0)]
        visited = set()

        while heap:
            time, x, y = heapq.heappop(heap)

            if x == ROW - 1 and y == COL - 1:
                return time

            if (x, y) in visited:
                continue
            visited.add((x, y))

            for dx, dy in directions:
                nx: int = x + dx
                ny: int = y + dy
                inGrid = nx >= 0 and ny >= 0 and nx < ROW and ny < COL
                visit = (nx, ny) in visited
                if not inGrid or visit:
                    continue
                if time + 1 >= grid[nx][ny]:
                    heapq.heappush(heap, (time + 1, nx, ny))
                else:
                    diff = grid[nx][ny] - time
                    if diff % 2 == 0:
                        heapq.heappush(heap, (grid[nx][ny] + 1, nx, ny))
                    else:
                        heapq.heappush(heap, (grid[nx][ny], nx, ny))

        return -1


def main() -> None:
    x = Solution()
    grid: List[List[int]] = [[0, 2, 4], [3, 2, 1], [1, 0, 4]]
    result: int = x.minimumTime(grid)
    print(result)


if __name__ == "__main__":
    main()
