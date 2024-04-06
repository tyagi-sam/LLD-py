from playingPiece import PlayingPiece
from Enums.pieceType import PieceType


class playingPieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.X)
