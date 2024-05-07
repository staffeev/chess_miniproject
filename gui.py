from figures import figures


CLASS_TO_SYMBOL = {
    (figures.Pawn, 0): "♟︎",
    (figures.Pawn, 1): "♙",
    (figures.Rook, 0): "♜",
    (figures.Rook, 1): "♖",
    (figures.Bishop, 0): "♝",
    (figures.Bishop, 1): "♗",
    (figures.Knight, 0): "♞",
    (figures.Knight, 1): "♘",
    (figures.King, 0): "♚",
    (figures.King, 1): "♔",
    (figures.Queen, 0): "♛",
    (figures.Queen, 1): "♕"
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
