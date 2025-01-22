#!/bin/python3


import sys
from PyQt5.QtWidgets import QApplication

from game import TicTacToe


def main() -> None:
    # Driver code
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
