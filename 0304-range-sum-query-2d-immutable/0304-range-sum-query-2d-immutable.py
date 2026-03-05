class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.mat = [[0 for _ in range(self.m+1)] for _ in range(self.n+1)]
        self.n += 1
        self.m += 1

        for i in range(1, self.n):
            for j in range(1, self.m):
                self.mat[i][j] = self.mat[i][j-1] + self.mat[i-1][j] - self.mat[i-1][j-1] + matrix[i-1][j-1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        tot = self.mat[row2+1][col2+1]
        add = self.mat[row1][col1]

        top_right = self.mat[row1][col2+1]
        bottom_left = self.mat[row2+1][col1]

        return tot - top_right - bottom_left + add

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)