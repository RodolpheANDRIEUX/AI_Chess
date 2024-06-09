import copy
from chess.move import Move
from chess.piece import King, Queen, Pawn, Bishop, Rook, Knight


def initialize_board():
    grid = [[None for _ in range(8)] for _ in range(8)]
    for i in range(8):
        grid[1][i] = Pawn('black', (1, i))
        grid[6][i] = Pawn('white', (6, i))
    grid[0][4] = King('black', (0, 4))
    grid[7][4] = King('white', (7, 4))
    grid[0][3] = Queen('black', (0, 3))
    grid[7][3] = Queen('white', (7, 3))
    grid[0][0] = Rook('black', (0, 0))
    grid[0][7] = Rook('black', (0, 7))
    grid[7][0] = Rook('white', (7, 0))
    grid[7][7] = Rook('white', (7, 7))
    grid[0][1] = Knight('black', (0, 1))
    grid[0][6] = Knight('black', (0, 6))
    grid[7][1] = Knight('white', (7, 1))
    grid[7][6] = Knight('white', (7, 6))
    grid[0][2] = Bishop('black', (0, 2))
    grid[0][5] = Bishop('black', (0, 5))
    grid[7][2] = Bishop('white', (7, 2))
    grid[7][5] = Bishop('white', (7, 5))
    return grid


class Board:
    def __init__(self):
        self.pieces = initialize_board()
        self.parallel_universe = initialize_board()
        self.valid_moves = [[False for _ in range(8)] for _ in range(8)]
        self.selected_piece = None
        self.move = None

    def move_piece(self, move):
        self.pieces[move.end_pos[0]][move.end_pos[1]] = move.piece
        self.pieces[move.start_pos[0]][move.start_pos[1]] = None
        move.piece.position = move.end_pos
        self.move = move  # store the move to animate it later in board_view.py

    def undo_move(self, move):
        self.pieces[move.start_pos[0]][move.start_pos[1]] = move.piece
        self.pieces[move.end_pos[0]][move.end_pos[1]] = None
        move.piece.position = move.start_pos

    def handle_square_selection(self, i, j):
        if self.selected_piece is not None:
            if self.is_valid_move(i, j):
                if self.valid_moves[i][j] == 'castle':
                    self.castle(i, j)
                asked_move = Move(self.selected_piece.position, (i, j), self.selected_piece)
                self.move_piece(asked_move)
                self.selected_piece.move(i, j)
                self.unselect()
                return
        self.unselect()
        selection_request = self.get_piece_at(i, j)
        if selection_request is not None:  # and selection_request.color == 'black':
            self.select_piece(i, j)

    def select_piece(self, i, j):
        self.selected_piece = self.pieces[i][j]
        self.selected_piece.select()
        self.valid_moves = self.selected_piece.valid_moves(self)
        for i in range(8):
            for j in range(8):
                if self.valid_moves[i][j]:
                    move = Move(self.selected_piece.position, (i, j), self.selected_piece)
                    if not self.king_safe(move):
                        self.valid_moves[i][j] = False

    def unselect(self):
        self.selected_piece = None
        self.valid_moves = [[False for _ in range(8)] for _ in range(8)]

    def get_piece_at(self, i, j):
        return self.pieces[i][j]  # return the piece object at i,j

    def is_valid_move(self, i, j):
        return self.valid_moves[i][j]  # return True if there is a valid move active on the board at i, j

    def king_safe(self, move):
        temp_pieces = copy.deepcopy(self.pieces)
        self.move_piece(move)
        safe = True
        for i in range(8):
            for j in range(8):
                piece = self.get_piece_at(i, j)
                if piece is not None and piece.color != move.piece.color:
                    valid_enemy_moves = piece.valid_moves(self)
                    for row in range(8):
                        for col in range(8):
                            if valid_enemy_moves[row][col]:
                                piece_threatened = self.get_piece_at(row, col)
                                if isinstance(piece_threatened, King) and piece_threatened.color == move.piece.color:
                                    safe = False
                                    break
        self.undo_move(move)
        self.pieces = temp_pieces
        return safe

    def castle(self, i, j):
        if i == 0:
            if j == 2:
                rook = self.get_piece_at(0, 0)
                rook_move = Move((0, 0), (0, 3), rook)
                self.move_piece(rook_move)
                rook.move(0, 3)
            elif j == 6:
                rook = self.get_piece_at(0, 7)
                rook_move = Move((0, 7), (0, 5), rook)
                self.move_piece(rook_move)
                rook.move(0, 5)
        elif i == 7:
            if j == 2:
                rook = self.get_piece_at(7, 0)
                rook_move = Move((7, 0), (7, 3), rook)
                self.move_piece(rook_move)
                rook.move(7, 3)
            elif j == 6:
                print("castle")
                rook = self.get_piece_at(7, 7)
                rook_move = Move((7, 7), (7, 5), rook)
                self.move_piece(rook_move)
                rook.move(7, 5)
        else:
            print("Invalid castle move")


# todo
"""
En passant, enrgistrer les coups, verifier le pat et le mat, verifier les echecs, ne pas castle si le roi 
est en echec
"""
