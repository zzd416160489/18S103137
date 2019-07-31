import position


def get_symbol_without_flag(piece_type):  # 获取棋子英文字母缩写
    dic = {
        "King": 'K',
        "Queen": 'Q',
        "Bishop": 'B',
        "Knight": 'N',
        "Rook": 'R',
        "Pawn": 'P',
        "Ball": 'O'     # 围棋棋子称为Ball
    }
    return dic.get(piece_type, 'X')         #如果未成功get棋子缩写，则使用X代表


class Piece:
    def __init__(self, piece_type ,player_number, piece_position = position.Position()):
        self.piece_type = piece_type
        self.position = piece_position          # 初始化棋子位置为(-1,-1)
        self.owner = player_number              # 初始化棋子的主人，1为player1，2为player2
        # 初始化棋子的表示符号
        self.symbol = '@='
        self.set_symbol(self.owner)

    def set_position(self, r, c):
        self.position = position.Position(r, c)

    def set_owner(self, owner_number):
        self.owner = owner_number

    def set_symbol(self, player_number):
        player_flag = '='
        if player_number == 1:
            player_flag = '+'
        elif player_number == 2:
            player_flag = '-'
        self.symbol = get_symbol_without_flag(self.piece_type) + player_flag
