from figures import *



CLASS_TO_SYMBOL = {
    (Pawn, 0): "♟︎",
    (Pawn, 1): "♙",
    (Rook, 0): "♜",
    (Rook, 1): "♖",
    (Bishop, 0): "♝",
    (Bishop, 1): "♗",
    (Knight, 0): "♞",
    (Knight, 1): "♘",
    (King, 0): "♚",
    (King, 1): "♔",
    (Queen, 0): "♛",
    (Queen, 1): "♕"
}



class Canvas:
    def __init__(self, board):
        self.board = board
    
    def draw(self):
        m = self.create_matrix()
        print(" ", *range(1, 9))
        for x, i in enumerate(m, 1):
            print(x, *i)

    def create_matrix(self):
        m = [[" " for _ in range(8)] for _ in range(8)]
        for fig in self.board.field:
            x, y = fig.pos.coords
            cl, color = fig.__class__, fig.color
            m[x][y] = CLASS_TO_SYMBOL[cl, color]
        return m
