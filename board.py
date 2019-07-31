import piece
import position


def place_chess(piece_type, piece_position, player_number):  # 放置一枚棋子————新建一枚棋子，赋其位置后加入棋子池
    new_piece = piece.Piece(piece_type, player_number)
    new_piece.position = piece_position
    Board.piecepool.append(new_piece)


class Board:
    n_chess = 8
    n_go = 19
    piecepool = []  # 选手棋子池
    board_matrix = []  # 棋盘矩阵,使用类变量完成全局变量的使命，进而各py文件均可访问

    def __init__(self, game_type):  # 初始化棋盘
        self.game_type = game_type
        if game_type == 'chess':
            self.init_chess_board()  # 初始化chess棋盘————将初始状态下的棋子放入棋子池（go棋盘初始状态不需要放置棋子）
        else:
            Board.piecepool = []
        self.set_board_matrix()  # 将棋子池的棋子显示在棋盘矩阵中

    def print_board(self):
        if self.game_type == 'chess':
            for r in range(Board.n_chess):
                for c in range(Board.n_chess):
                    print(Board.board_matrix[r][c] + '  ', end='')
                print()
        elif self.game_type == 'go':
            for r in range(Board.n_go):
                for c in range(Board.n_go):
                    print(Board.board_matrix[r][c] + '  ', end='')
                print()

    def get_piece_number(self, player_number):
        n = 0
        for piece_iter in Board.piecepool:
            if piece_iter.owner == player_number:
                n += 1
        return n

    def init_chess_board(self):
        # 放置player1的初始棋子
        place_chess('King', position.Position(0, 4), 1)
        place_chess('Queen', position.Position(0, 3), 1)
        place_chess('Bishop', position.Position(0, 2), 1)
        place_chess('Bishop', position.Position(0, 5), 1)
        place_chess('Knight', position.Position(0, 1), 1)
        place_chess('Knight', position.Position(0, 6), 1)
        place_chess('Rook', position.Position(0, 0), 1)
        place_chess('Rook', position.Position(0, 7), 1)
        for i in range(8):
            place_chess('Pawn', position.Position(1, i), 1)
        # 放置player2的初始棋子
        place_chess('King', position.Position(7, 4), 2)
        place_chess('Queen', position.Position(7, 3), 2)
        place_chess('Bishop', position.Position(7, 2), 2)
        place_chess('Bishop', position.Position(7, 5), 2)
        place_chess('Knight', position.Position(7, 1), 2)
        place_chess('Knight', position.Position(7, 6), 2)
        place_chess('Rook', position.Position(7, 0), 2)
        place_chess('Rook', position.Position(7, 7), 2)
        for i in range(8):
            place_chess('Pawn', position.Position(6, i), 2)

    def set_board_matrix(self):
        if self.game_type == 'chess':
            Board.board_matrix = [['. '] * Board.n_chess for i in range(Board.n_chess)]
        elif self.game_type == 'go':
            Board.board_matrix = [['. '] * Board.n_go for i in range(Board.n_go)]
        for iter_piece in Board.piecepool:
            Board.board_matrix[iter_piece.position.r][iter_piece.position.c] = iter_piece.symbol
