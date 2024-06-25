import random
from chess.move import Move


class Ai:
    def __init__(self, board):
        self.board = board
        self.color = 'black'

    def get_possible_moves(self, board):
        moves = []
        for i in range(8):
            for j in range(8):
                piece = board.get_piece_at(i, j)
                if piece is not None and piece.color == self.color:
                    board.select_piece(i, j)
                    for x in range(8):
                        for y in range(8):
                            if board.valid_moves[x][y]:
                                moves.append(Move((i, j), (x, y), piece))
        board.unselect()
        return moves

    def play_random(self):
        possible = self.get_possible_moves(self.board)
        if not possible:
            return
        move = random.choice(possible)
        print(move.piece.position)
        self.board.select_piece(move.piece.position[0], move.piece.position[1])
        self.board.play(move.end_pos[0], move.end_pos[1])
        self.board.unselect()
