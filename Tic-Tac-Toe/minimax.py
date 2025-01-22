class MiniMax:
    def __init__(self) -> None:
        self.player = "X"
        self.computer = "O"

    def setSymbols(self, player, computer):
        self.player = player
        self.computer = computer

    def isMovesLeft(self, board):
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    return True
        return False

    def evaluate(self, b):
        for row in range(3):
            if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
                if b[row][0] == self.computer:
                    return 10
                elif b[row][0] == self.player:
                    return -10

        for col in range(3):
            if b[0][col] == b[1][col] and b[1][col] == b[2][col]:
                if b[0][col] == self.computer:
                    return 10
                elif b[0][col] == self.player:
                    return -10

        if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
            if b[0][0] == self.computer:
                return 10
            elif b[0][0] == self.player:
                return -10

        if b[0][2] == b[1][1] and b[1][1] == b[2][0]:
            if b[0][2] == self.computer:
                return 10
            elif b[0][2] == self.player:
                return -10

        return 0

    def minimax(self, board, depth, isMax):
        score = self.evaluate(board)

        if score == 10:
            return score - depth

        if score == -10:
            return score + depth

        if not (self.isMovesLeft(board)):
            return 0

        if isMax:
            best = -1000

            for i in range(3):
                for j in range(3):
                    if board[i][j] == "_":
                        board[i][j] = self.computer

                        best = max(best, self.minimax(board, depth + 1, not isMax))

                        board[i][j] = "_"
            return best

        else:
            best = 1000

            for i in range(3):
                for j in range(3):
                    if board[i][j] == "_":
                        board[i][j] = self.player

                        best = min(best, self.minimax(board, depth + 1, not isMax))

                        board[i][j] = "_"
            return best

    def findBestMove(self, board):
        bestVal = -1000
        bestMove = (-1, -1)

        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = self.computer

                    moveVal = self.minimax(board, 0, False)

                    board[i][j] = "_"

                    if moveVal > bestVal:
                        bestMove = (i, j)
                        bestVal = moveVal

        return bestMove
