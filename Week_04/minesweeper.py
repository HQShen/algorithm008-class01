class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = len(board), len(board[0])
        new_board = board.copy()
        a, b = click
        if board[a][b] == 'M':
            new_board[a][b] = 'X'
        if board[a][b] == 'E':
            self.update(a, b, new_board)
        return new_board

    def update(self, a, b, new_board):
        row, col = len(new_board), len(new_board[0])
        inds = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        neighbor_boom = 0
        for ind in inds:
            if 0 <= a+ind[0] < row and 0<= b+ind[1] < col:
                neighbor_boom += new_board[a+ind[0]][b+ind[1]] == 'M'
        if new_board[a][b] == 'E' and not neighbor_boom:
            new_board[a][b] = 'B'
            for ind in inds:
                if 0 <= a+ind[0] < row and 0<= b+ind[1] < col:
                    self.update(a+ind[0], b+ind[1], new_board)
        if neighbor_boom:
            new_board[a][b] = str(neighbor_boom)
            
        return