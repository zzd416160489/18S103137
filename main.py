import game
import os


flag = 1
while flag:
    os.system('cls')
    print('请输入您想要玩的游戏(chess or go)：\n获取帮助请输入help，退出请输入exit')
    command_str = input()
    if command_str == 'help':
        print('游戏帮助：\n本程序实现国际象棋chess与围棋go的基础功能，祝你玩得开心！')
        os.system('pause')
    elif command_str == 'exit':
        flag = 0
    elif command_str == 'chess' or command_str == 'go':
        your_game = game.Game(command_str)
        your_game.start_game()
    else:
        print('这里没有您想要玩的' + command_str + '游戏，请重新输入！')
        os.system('pause')