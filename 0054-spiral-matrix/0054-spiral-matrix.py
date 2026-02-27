class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        
        n = len(matrix[0])
        answer = []
        direction = [[1,0],[0,-1],[-1,0],[0,1]]
        visited = []
        for i in range(m):
            visited.append([0]*n)
        def traverse(coord, index):
            if coord[0] >= m or coord[0] < 0 or coord[1] >= n or coord[0] < 0 or visited[coord[0]][coord[1]] == 1:
                return
            answer.append(matrix[coord[0]][coord[1]])
            visited[coord[0]][coord[1]] = 1
            coord2 = [a + b for a, b in zip(coord, direction[index])]
            if coord2[0] >= m or coord2[0] < 0 or coord2[1] >= n or coord2[0] < 0 or visited[coord2[0]][coord2[1]] == 1:
                index = (index + 1) % 4
            coord2 = [a + b for a, b in zip(coord, direction[index])]
            traverse(coord2, index)
        traverse([0,0],3)
        return answer        