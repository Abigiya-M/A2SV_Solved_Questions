class Solution:
    def totalNQueens(self, n: int) -> int:
        self.output = 0
        placed: list[tuple[int, int]] = []
        self.dfs(0, n, placed)
        return self.output

    output: int = 0
    def dfs(self, row: int, n: int, placed: list[tuple[int, int]]) -> None:
        if row == n:
            self.output += 1
            return
        for col in range(n):
            can_place: bool = True
            for x, y in placed:
                if col == y or row == x or (abs(col - y) == abs(row - x)):
                    can_place = False
                    break
            if not can_place: continue
            placed.append((row, col))
            self.dfs(row + 1, n, placed)
            placed.pop()