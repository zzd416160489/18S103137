import board
import piece
import position
import player
import time
import os


class Game:
    def __init__(self, game_type):
        self.play_history = []  # 走棋历史记录
        self.player_round = 1  # 走棋回合
        self.player1 = 0
        self.player2 = 0
        self.game_type = game_type
        self.board = board.Board(game_type)
        self.while_flag = 1  # 游戏回合循环开关

    def start_game(self):
        os.system('cls')
        str_player_name = input('请输入第一位选手的昵称：')
        self.player1 = player.Player(1, str_player_name)
        str_player_name = input('请输入第二位选手的昵称：')
        while str_player_name == self.player1.name:
            print('两位选手的昵称不能相同，请重新输入第二位选手的昵称：')
            str_player_name = input()
        self.player2 = player.Player(2, str_player_name)
        print(self.player1.name + ' vs ' + self.player2.name)
        time.sleep(0.3)
        print(self.game_type + '游戏开始！')
        time.sleep(0.3)

        while self.while_flag:
            if self.player_round % 2 == 1:
                self.while_flag = self.player_action(self.player1)
            else:
                self.while_flag = self.player_action(self.player2)

        os.system('cls')
        print("本局游戏手动结束，现在回放走棋历史")
        for play_record in self.play_history:
            print(play_record)
        os.system('pause')

    def player_action(self, piece_player):
        # 清屏并显示对战基础信息
        os.system('cls')
        print('player1:' + self.player1.name + ' vs player2:' + self.player2.name)
        print('当前棋子数: ' + self.player1.name + ':' + self.board.get_piece_number(1).__str__() + ', ' \
              + self.player2.name + ':' + self.board.get_piece_number(2).__str__())

        self.board.set_board_matrix()  # 更新棋子池在棋盘的矩阵显示
        self.board.print_board()  # 显示棋盘

        # 玩家行动提示
        print('现在轮到' + piece_player.name + '行动：')
        if self.game_type == 'chess':
            print('您可以输入(r1,c1,r2,c2)，代表将(r1,c1)位置处的棋子移动到(r2,c2)，输入"end"则退出本局游戏')
        else:
            print('您可以输入(r,c)，代表将棋子下在(r,c)处，输入"end"则退出本局游戏')
        str_command = input()

        # 处理手动结束游戏指令
        if str_command == 'end':
            return 0

        # 执行玩家输入的下棋指令
        if self.game_type == 'chess':
            if self.player_round % 2 == 1:
                self.player1.move_chess(str_command)
            else:
                self.player2.move_chess(str_command)
        else:
            if self.player_round % 2 == 1:
                self.player1.place_go(str_command)
            else:
                self.player2.place_go(str_command)

        # 玩家操作的每一步都会被写入史册
        if self.player_round % 2 == 1:
            player_number_str = 'player1'
        else:
            player_number_str = 'player2'
        self.play_history.append('round ' + self.player_round.__str__() + '   ' + player_number_str + ':' + str_command)
        self.player_round += 1
        return 1
