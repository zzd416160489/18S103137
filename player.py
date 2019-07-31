import action
import board
import position
import os


class Player:
    def __init__(self, player_number, name):
        self.player_number = player_number  # 选手编号
        self.name = name  # 选手昵称
        self.action = action.Action(self.player_number)

    def move_chess(self, str_command):
        [r1, c1, r2, c2] = str_command.split(',', 4)
        pass_flag1 = 0
        # 检验(r1,c1)是否有属于此player的棋子
        for piece_iter in board.Board.piecepool:
            if piece_iter.position.r == int(r1) and piece_iter.position.c == int(c1) and \
                    piece_iter.owner == self.player_number:
                pass_flag1 = 1
                break
        # 检验(r2,c2)是否可以放下此棋子(这一格没有自己的棋子)
        pass_flag2 = 1
        for piece_iter_1 in board.Board.piecepool:
            if piece_iter_1.position.r == int(r2) and piece_iter_1.position.c == int(c2):
                if piece_iter_1.owner == self.player_number:
                    pass_flag2 = 0
                    break
        # 如果(r1,c1)处有自己的棋子，且(r2,c2)没有自己的棋子则判断(r2,c2)是否有敌方棋子
        if pass_flag1 == 1 and pass_flag2 == 1:
            for piece_iter_1 in board.Board.piecepool:
                if piece_iter_1.position.r == int(r2) and piece_iter_1.position.c == int(c2):
                    if piece_iter_1.owner != self.player_number:
                        # 当(r2,c2)处有敌方棋子时，吃掉该棋子
                        board.Board.piecepool.remove(piece_iter_1)
                        break
            # 将自己移到(r2,c2)处
            for piece_iter in board.Board.piecepool:
                if piece_iter.position.r == int(r1) and piece_iter.position.c == int(c1):
                    piece_iter.position = position.Position(int(r2),int(c2))
                    break
        else:
            print('你并没有在本回合做出有效动作')
            os.system('pause')

    def place_go(self,str_command):
        # 放置围棋棋子
        [r,c] = str_command.split(',',2)
        # 检验(r,c)处有无棋子
        check_flag = 0
        for piece_iter in board.Board.piecepool:
            if piece_iter.position.r == int(r) and piece_iter.position.c == int(c):
                print('你并没有在本回合做出有效动作')
                check_flag = 1
                break
        if check_flag == 0:
            board.place_chess('Ball',position.Position(int(r),int(c)),self.player_number)