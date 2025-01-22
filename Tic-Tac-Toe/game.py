from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QMessageBox

from minimax import MiniMax


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.board = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"],
        ]
        self.minimaxAI = MiniMax()

    def init_ui(self):
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(100, 100, 300, 300)

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.buttons = [[QPushButton("") for _ in range(3)] for _ in range(3)]
        self.player = "X"
        self.computer = "O"

        for i in range(3):
            for j in range(3):
                button = self.buttons[i][j]
                button.setFixedSize(100, 100)
                button.setStyleSheet("font-size: 24px;")
                button.clicked.connect(lambda checked, x=i, y=j: self.on_click(x, y))
                self.grid_layout.addWidget(button, i, j)

    def on_click(self, x, y):
        self.board[x][y] = self.player

        button = self.buttons[x][y]
        if button.text() != "":
            return
        button.setText(self.player)

        if self.check_winner():
            QMessageBox.information(self, "Game Over", "Player wins!")
            self.reset_board()
        elif self.check_draw():
            QMessageBox.information(self, "Game Over", "It's a draw!")
            self.reset_board()
        else:
            self.computerTurn()

    def playerTurn(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setEnabled(True)

    def computerTurn(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setEnabled(False)

        x, y = self.minimaxAI.findBestMove(self.board)

        self.board[x][y] = self.computer
        button = self.buttons[x][y]
        button.setText(self.computer)

        if self.check_winner():
            QMessageBox.information(self, "Game Over", "Computer wins!")
            self.reset_board()
        elif self.check_draw():
            QMessageBox.information(self, "Game Over", "It's a draw!")
            self.reset_board()
        else:
            self.playerTurn()

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "_":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "_":
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "_":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "_":
            return True

        return False

    def check_draw(self):
        return all(self.board[i][j] != "_" for i in range(3) for j in range(3))

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setText("")
                self.board[i][j] = "_"

        self.swap_symbols()

        if self.computer == "X":
            self.computerTurn()
        else:
            self.playerTurn()

    def swap_symbols(self):
        self.player, self.computer = self.computer, self.player
        self.minimaxAI.setSymbols(self.player, self.computer)
