from playingPiece import PlayingPiece
from Enums.pieceType import PieceType


class playingPieceO(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.O)
