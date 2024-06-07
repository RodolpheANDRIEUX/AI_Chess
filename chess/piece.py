class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def valid_moves(self, board):
        # Renvoie une liste des mouvements valides pour la pièce
        pass

    def __str__(self):
        return f"{self.color} {self.__class__.__name__}"


class King(Piece):
    # Implémentation spécifique pour le Roi
    pass

# Idem pour Queen, Bishop, Knight, Rook, Pawn
