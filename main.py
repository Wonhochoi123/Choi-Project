from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
import random
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.core.audio import SoundLoader
from kivy.uix.pagelayout import PageLayout
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.properties import StringProperty
from kivy.config import Config
from kivy.uix.relativelayout import RelativeLayout
import numpy as np
# from tkinter import Tk
import copy
# win= Tk()
global is_ai
is_ai=None
global start
start=False
global num_cols

num_cols=4
global num_cols_initial
num_cols_initial=num_cols

# win.geometry("650x250")
#
# screen_width = win.winfo_screenwidth()
# screen_height = win.winfo_screenheight()
#
# if screen_height<screen_width*2:
#     print(type(screen_height))
#     Config.set('graphics', 'resizable', '0')
#     Config.set('graphics', 'width', str(int(screen_height/2)))
#     Config.set('graphics', 'height', str(int(screen_height)))
# else:
#     Config.set('graphics', 'resizable', '0')
#     Config.set('graphics', 'width', str(int(screen_width)))
#     Config.set('graphics', 'height', str(int(screen_width*2)))
#
#
# Config.set('graphics', 'width', str(int(screen_height/2*0.91)))
# Config.set('graphics', 'height', str(int(screen_height*0.91)))



import time
import glob
bgm_list=glob.glob('resources/bgm/*')
bgm_list_now=[]
global playtime
playtime=0

class TimeFrame(FloatLayout):
    background_image = ObjectProperty(
        Image(source="resources/timeframe/1.png"))

class TimeFrameMy(FloatLayout):
    background_image = ObjectProperty(
        Image(source="resources/timeframe/2.png"))
class CircularAnchor(AnchorLayout):
    pass
class GobbSocket(AnchorLayout):
    background_image = ObjectProperty(
        Image(source="resources/gobb_socket/1.png"))

class CustomLayout(AnchorLayout):
    background_image = ObjectProperty(
        Image(source="resources/white_marble2/white_marb4.png"))

class MyLabel(Image):
    text = StringProperty('')
    def on_text(self, *_):
        l = Label(text=self.text,font_name="resources/fonts/Adonais Regular.ttf",color=[0.80,0.80,0.80,1])
        l.font_size = '1000dp'  # something that'll give texture bigger than phone's screen size
        l.texture_update()
        self.texture = l.texture


from kivy.uix.screenmanager import ScreenManager, Screen




class MainWindow(Screen):




    def Tutorial_4x4(self):
        global start
        global num_cols
        global is_ai
        num_cols=4
        start=True
        is_ai = True
        start_bell = SoundLoader.load('resources/sound effects/Door-Bell-Ding-A1-www.fesliyanstudios.com.mp3')
        if start_bell:
            start_bell.volume = 0.5
            start_bell.play()

        # Clock.schedule_interval(update, 1.0 / 20.0)

    def Tutorial_3x3(self):
        global start
        global num_cols
        global is_ai
        global board
        num_cols=3
        start=True
        is_ai = True
        start_bell = SoundLoader.load('resources/sound effects/Door-Bell-Ding-A1-www.fesliyanstudios.com.mp3')
        if start_bell:
            start_bell.volume = 0.5
            start_bell.play()
        # Clock.schedule_interval(update, 1.0 / 20.0)
    def Local_4x4(self):
        global start
        global num_cols
        global is_ai
        num_cols = 4
        start = True
        is_ai = False
        start_bell = SoundLoader.load('resources/sound effects/Door-Bell-Ding-A1-www.fesliyanstudios.com.mp3')
        if start_bell:
            start_bell.volume = 0.5
            start_bell.play()
        # Clock.schedule_interval(update, 1.0 / 20.0)
    def Local_3x3(self):
        global start
        global num_cols
        global is_ai
        num_cols = 3
        start = True
        is_ai = False
        start_bell = SoundLoader.load('resources/sound effects/Door-Bell-Ding-A1-www.fesliyanstudios.com.mp3')
        if start_bell:
            start_bell.volume = 0.5
            start_bell.play()

        # Clock.schedule_interval(update, 1.0 / 20.0)
    pass
class SecondWindow(Screen):
    # start=True
    pass

class SecondWindow1(Screen):

    # start=True
    pass

class WindowManager(ScreenManager):
    pass
class TheLabApp(App):
    pass



class Game(BoxLayout):

    # pass
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        def update(self):
            global to_time
            global selected_g
            global selected_my
            global selected_opo
            global turn
            global result
            global is_ai
            global start
            global num_cols
            global num_cols_initial
            now_time = time.time()
            if start != True:
                to_time = now_time + 30
            timeleft = to_time - now_time

            color_change = np.array([177 - 100 * (timeleft / 30), 152 * (timeleft / 30), timeleft / 30 * 255]) / 255
            color_change = list(color_change)
            if turn > 0:
                time_wid_my.size_hint = [(timeleft) / 28, 0.1]
                time_wid_my.background_color = color_change + [1]
                face_box_player.col = color_change + [0.6]
                myturnsign.opacity = (timeleft) / 30
                myturnsign.opacity = (timeleft) / 30
                yourturnsign.opacity = 0
            elif turn < 0:
                time_wid_opo.size_hint = [(timeleft) / 28, 0.1]
                time_wid_opo.background_color = color_change + [1]
                face_box_opo.col = color_change + [0.6]
                myturnsign.opacity = 0
                yourturnsign.opacity = (timeleft) / 30
                if timeleft < 28:
                    AImoves()
            if timeleft < 0:
                if selected_g > 0:
                    selected_my = selected_g
                elif selected_g < 0:
                    selected_opo = selected_g
                selected_g = 0
                switch_turn()
            if num_cols_initial!=num_cols:
                reset(self)
                num_cols_initial=num_cols
            global bgm_list_now
            global bgm_list
            if len(bgm_list_now)==0:
                bgm_list_now=bgm_list.copy()
            global time_when_play
            global playtime
            global playtime_this
            global bgm_now
            if playtime<=1:
                time_when_play=time.time()
                print(time_when_play)
                bgm_now=SoundLoader.load(bgm_list_now.pop())
                bgm_now.volume = 0.5
                bgm_now.play()
                playtime_this=bgm_now.length
            playtime =playtime_this+time_when_play-time.time()





        Clock.schedule_interval(update, 1.0 / 20.0)


        def reset(self):
            global num_cols
            global initial_my
            global initial_opo
            for i in range(len(initial_opo)):
                dict_opo_box[f'{i}'].background_normal = f"resources/gobbs/{gobb_name}_0_4.png"
                dict_opo_box[f'{i}'].background_down = f"resources/gobbs/{gobb_name}_0_4.png"
                dict_opo_box[f'{i}'].size_hint = [0.85, 0.85]
            for i in range(num_cols):
                for k in range(num_cols):
                    dict_board[f'{i},{k}'].background_normal = f'resources/{board_name}/empty.png'
                    dict_board[f'{i},{k}'].background_down = f'resources/{board_name}/empty.png'
            for i in range(len(initial_my)):
                dict_my_box[f'{i}'].background_normal = f"resources/gobbs/{gobb_name}_1_4.png"
                dict_my_box[f'{i}'].background_down = f"resources/gobbs/{gobb_name}_1_4.png"
                dict_my_box[f'{i}'].size_hint = [0.85, 0.85]
            global board
            global dict_size_hint
            dict_size_hint = {4: [0.85, 0.85], 3: [0.7, 0.7], 2: [0.55, 0.55], 1: [0.4, 0.4], 0: [0, 0]}
            board = [{k: [0] for k in range(num_cols)} for i in range(num_cols)]

            initial_my = [[k + 1 for k in range(num_cols)] for i in range(num_cols - 1)]
            initial_opo = [[(k + 1) * -1 for k in range(num_cols)] for i in range(num_cols - 1)]
            global turn
            turn_list = [1, -1]
            time_wid_opo.background_color = [1, 1, 1, 1]
            time_wid_my.background_color = [1, 1, 1, 1]
            time_wid_opo.size_hint = [30 / 28, 0.1]
            time_wid_my.size_hint = [30 / 28, 0.1]
            turn = random.choice(turn_list)
            global now_time
            global to_time
            global timeleft
            now_time = time.time()
            to_time = now_time + 30
            timeleft = to_time - now_time











        global turn
        global board
        turn_list=[1,-1]
        turn=random.choice(turn_list)
        print(turn)
        global dict_size_hint
        dict_size_hint={4:[0.85,0.85], 3: [0.7,0.7],2:[0.55,0.55],1:[0.4,0.4], 0:[0,0]}
        global num_cols
        if num_cols==3:
            board = [{k: [0] for k in range(3)} for i in range(3)]
        elif num_cols==4:
            board = [{k: [0] for k in range(4)} for i in range(4)]

        global selected_g
        selected_g = 0
        global initial_opo
        global initial_my
        global gobb_name
        global board_name
        global selected_my
        global selected_opo
        gobb_name = 'gobb_marb'
        board_name = 'white_marble2'
        initial_my=[[k+1 for k in range(num_cols)] for i in range(num_cols-1)]
        initial_opo=[[(k+1)*-1 for k in range(num_cols)] for i in range(num_cols-1)]
        selected_my=0
        selected_opo=0
        self.orientation = 'vertical'


        grabbing_sfx = SoundLoader.load('resources/sound effects/grab.wav')
        block = SoundLoader.load(f'resources/sound effects/block.wav')



        def AIpress(where):
            where.state = 'down'
            where.trigger_action(0.1)
        def AImoves():
            global turn
            global board
            global is_ai
            global num_cols
            global initial_opo
            global ai_score
            global player_score
            global pos_num1
            global pos_num2
            global pos_num3
            global pos_num4
            # num_cols
            gob_but_list=list(dict_opo_box.keys())
            board_list=list(dict_board.keys())
            score_dict={}
            First=True
            if (turn ==-1)&(is_ai==True):
                for i in range(num_cols):
                    for k in range(num_cols):
                        if board[i][k][-1]!=0:
                            First=False
                if First==True:
                    print('First!')
                    gob_choice = random.choice(gob_but_list)
                    AIpress(dict_opo_box[gob_choice])
                    board_choice = random.choice(board_list)
                    AIpress(dict_board[board_choice])
                else:
                    avbl_gob = [i[-1] for i in initial_opo]
                    for i in range(num_cols):
                        for k in range(num_cols):
                            for p in [i for i in range(len(avbl_gob))]:
                                sim_board = copy.deepcopy(board)
                                exp_score = 0
                                if abs(sim_board[i][k][-1]) < abs(avbl_gob[p]):
                                    sim_board[i][k].append(avbl_gob[p])

                                    check_win(tile=f'{i},{k}',board=sim_board)
                                    if result=='lose':
                                        AIpress(dict_opo_box[str(p)])
                                        AIpress(dict_board[f'{i},{k}'])
                                        return
                            sim_board = copy.deepcopy(board)

                            if sim_board[i][k][-1]<0:
                                check_win(tile=f'{i},{k}', board=board)
                                if result!='win':
                                    for ii in range(num_cols):
                                        for kk in range(num_cols):
                                            if abs(sim_board[ii][kk][-1]) < abs(board[i][k][-1]):
                                                sim_board = copy.deepcopy(board)
                                                select_sim = sim_board[i][k].pop()
                                                sim_board[ii][kk].append(select_sim)

                                                check_win(tile=f'{ii},{kk}', board=sim_board)

                                                if result == 'lose':
                                                    print(sim_board)
                                                    AIpress(dict_board[f'{i},{k}'])
                                                    AIpress(dict_board[f'{ii},{kk}'])
                                                    return

                            sim_board = copy.deepcopy(board)
                            for p in [i for i in range(len(avbl_gob))]:
                                if abs(sim_board[i][k][-1]) < abs(avbl_gob[p]):
                                    ###########
                                    sim_board = copy.deepcopy(board)
                                    exp_score = 0
                                    exp_score = exp_score + 800

                                    check_win(tile=f'{i},{k}', board=board)
                                    is_danger1=False
                                    is_danger2=False
                                    is_danger3=False
                                    is_danger4=False
                                    if pos_num1==3:
                                        is_danger1=True
                                    if pos_num2==3:
                                        is_danger2=True
                                    if pos_num3==3:
                                        is_danger3=True
                                    if pos_num4==3:
                                        is_danger4=True

                                    exp_score=exp_score+player_score-ai_score
                                    sim_board = copy.deepcopy(board)
                                    sim_board[i][k].append(avbl_gob[p])
                                    check_win(tile=f'{i},{k}', board=sim_board)
                                    if is_danger1==True:
                                        if pos_num1==2:
                                            AIpress(dict_opo_box[str(p)])
                                            AIpress(dict_board[f'{i},{k}'])
                                            return
                                    if is_danger2 == True:
                                        if pos_num2 == 2:
                                            AIpress(dict_opo_box[str(p)])
                                            AIpress(dict_board[f'{i},{k}'])
                                            return
                                    if is_danger3 == True:
                                        if pos_num3 == 2:
                                            AIpress(dict_opo_box[str(p)])
                                            AIpress(dict_board[f'{i},{k}'])
                                            return
                                    if is_danger4 == True:
                                        if pos_num4 == 2:
                                            AIpress(dict_opo_box[str(p)])
                                            AIpress(dict_board[f'{i},{k}'])
                                            return

                                    exp_score=exp_score+ai_score-player_score
                                    score_dict[f'g_{p}_{i},{k}']=exp_score
                                    # pos_num_before=pos_num1
                            sim_board = copy.deepcopy(board)

                            if sim_board[i][k][-1]<0:
                                check_win(tile=f'{i},{k}', board=board)

                                pos_num_before1=pos_num1
                                pos_num_before2=pos_num2
                                pos_num_before3=pos_num3
                                pos_num_before4=pos_num4

                                player_score_before=player_score
                                ai_score_before=ai_score
                                # if pos_num_after-pos_num_before==1:
                                #     ai_score=ai_score*3

                                print('before: ',exp_score)
                                is_danger1 = False
                                is_danger2 = False
                                is_danger3 = False
                                is_danger4 = False
                                if pos_num1 == 3:
                                    is_danger1 = True
                                if pos_num2 == 3:
                                    is_danger2 = True
                                if pos_num3 == 3:
                                    is_danger3 = True
                                if pos_num4 == 3:
                                    is_danger4 = True

                                if result!='win':
                                    for ii in range(num_cols):
                                        for kk in range(num_cols):
                                            if abs(sim_board[ii][kk][-1]) < abs(board[i][k][-1]):
                                                sim_board = copy.deepcopy(board)
                                                select_sim = sim_board[i][k].pop()
                                                sim_board[ii][kk].append(select_sim)

                                                check_win(tile=f'{ii},{kk}', board=sim_board)
                                                pos_num_after1 = pos_num1
                                                pos_num_after2 = pos_num1
                                                pos_num_after3 = pos_num1
                                                pos_num_after4 = pos_num1

                                                if is_danger1 == True:
                                                    if pos_num1 == 2:
                                                        AIpress(dict_board[f'{i},{k}'])
                                                        AIpress(dict_board[f'{ii},{kk}'])
                                                        return
                                                if is_danger2 == True:
                                                    if pos_num2 == 2:
                                                        AIpress(dict_board[f'{i},{k}'])
                                                        AIpress(dict_board[f'{ii},{kk}'])
                                                        return
                                                if is_danger3 == True:
                                                    if pos_num3 == 2:
                                                        AIpress(dict_board[f'{i},{k}'])
                                                        AIpress(dict_board[f'{ii},{kk}'])
                                                        return
                                                if is_danger4 == True:
                                                    if pos_num4 == 2:
                                                        AIpress(dict_board[f'{i},{k}'])
                                                        AIpress(dict_board[f'{ii},{kk}'])
                                                        return

                                                is_danger1 = False
                                                is_danger2 = False
                                                is_danger3 = False
                                                is_danger4 = False


                                                exp_score = ai_score -ai_score_before + player_score_before - player_score
                                                if pos_num_after1 - pos_num_before1 == 1:
                                                    if pos_num_after1==2:
                                                        exp_score=-100000000
                                                    exp_score = exp_score + 400
                                                if pos_num_after2 - pos_num_before2 == 1:
                                                    if pos_num_after2==2:
                                                        exp_score=-100000000
                                                    exp_score=exp_score+400
                                                if pos_num_after3 - pos_num_before3 == 1:
                                                    if pos_num_after3==2:
                                                        exp_score=-100000000
                                                    exp_score=exp_score=400
                                                if pos_num_after4 - pos_num_before4 == 1:
                                                    if pos_num_after4==2:
                                                        exp_score=-100000000
                                                    exp_score=exp_score+400

                                                if (pos_num_after1-pos_num_before1==1)&( pos_num_after1>2 ):
                                                        exp_score=-10000

                                                if (pos_num_after2-pos_num_before2==1)&( pos_num_after2>2 ):
                                                        exp_score=-10000

                                                if (pos_num_after3-pos_num_before3==1)&( pos_num_after3>2 ):
                                                        exp_score=-10000

                                                if (pos_num_after4-pos_num_before4==1)&( pos_num_after4>2 ):
                                                        exp_score=-10000


                                                score_dict[f'{i},{k}_{ii},{kk}'] = exp_score





                    max_score=max(score_dict.values())
                    print(score_dict)

                    choice=random.choice([key for key in score_dict.keys() if score_dict[key]==max_score])
                    print(choice)
                    if choice[:1]=='g':
                        gob_choice=choice.split('_')[-2]
                        board_choice=choice.split('_')[-1]
                        AIpress(dict_opo_box[gob_choice])
                        AIpress(dict_board[board_choice])
                    else:
                        gob_choice = choice.split('_')[-2]
                        board_choice = choice.split('_')[-1]
                        AIpress(dict_board[gob_choice])
                        AIpress(dict_board[board_choice])




                    return

                    # gob_choice = random.choice(gob_but_list)
                    # AIpress(dict_opo_box[gob_choice])
                    # board_choice = random.choice(board_list)
                    # AIpress(dict_board[board_choice])



        def switch_turn():
            global turn
            global selected_opo
            global selected_my
            global selected_g
            if turn ==1:
                turn=-1
                selected_g=selected_opo
                selected_opo=0
            elif turn ==-1:
                turn=1
                selected_g=selected_my
                selected_my=0
            print('new tern: ', turn)
            time_wid_opo.background_color = [1, 1, 1, 1]
            time_wid_my.background_color = [1, 1, 1, 1]
            face_box_player.col = [1, 1, 1, 0]
            face_box_opo.col = [1, 1, 1, 0]

            global to_time
            to_time = time.time() + 30

        def check_win(tile,board):
            # global board
            global result
            num_cols= len(board)
            row_val=int(tile.split(',')[0])
            col_val=int(tile.split(',')[-1])
            result ='None'
            global ai_score
            global player_score
            global pos_num1
            global pos_num2
            global pos_num3
            global pos_num4
            pos_num1=0
            neg_num=0

            ai_score=0
            player_score=0
            player_score1=0
            player_score2=0
            player_score3=0
            player_score4=0
            ai_score1=0
            ai_score2=0
            ai_score3=0
            ai_score4=0

            for row in board[row_val].values():
                if row[-1]>0:
                    player_score1=player_score1+row[-1]
                    pos_num1=pos_num1+1
                elif row[-1]<0:
                    ai_score1=ai_score1+abs(row[-1])
                    neg_num=neg_num+1
                if pos_num1==num_cols:
                    result='win'
                    break
                if neg_num==num_cols:
                    result='lose'
                    break

            if pos_num1 == 3:
                # player_score1=player_score1*2
                if ai_score1 == 4:
                    ai_score1=1000
                    player_score1 = 0

            if neg_num == 3:
                # ai_score1=ai_score1*2

                if player_score1 == 4:
                    player_score1=1000
                    ai_score1 = 0

            pos_num2=0
            neg_num=0
            for column in board:
                if column[col_val][-1] >0:
                    player_score2=player_score2+column[col_val][-1]
                    pos_num2 = pos_num2 + 1
                elif column[col_val][-1] < 0:
                    ai_score2=ai_score2+abs(column[col_val][-1])
                    neg_num = neg_num + 1
                if pos_num2 == num_cols:
                    result = 'win'
                    break
                if neg_num == num_cols:
                    result = 'lose'
                    break
            if pos_num2 == 3:
                # player_score2=player_score2*2
                if ai_score2 == 4:
                    ai_score2 = 1000
                    player_score2 = 0
            if neg_num == 3:
                # ai_score2=ai_score2*2
                if player_score2 == 4:
                    player_score2=1000
                    ai_score2 = 0
            pos_num3 = 0
            neg_num = 0
            if (row_val==col_val):
                for i in range(num_cols):
                    if board[i][i][-1] > 0:
                        player_score3 =player_score3+ board[i][i][-1]
                        pos_num3 = pos_num3 + 1
                    if board[i][i][-1] < 0:
                        ai_score3 =ai_score3+abs(board[i][i][-1])
                        neg_num = neg_num + 1
                    if pos_num3 == num_cols:
                        result = 'win'
                        break
                    if neg_num == num_cols:
                        result = 'lose'
                        break
                if pos_num3 == 3:
                    # player_score3 = player_score3 * 2
                    if ai_score3 == 4:
                        ai_score3=1000
                        player_score3 = 0
                if neg_num == 3:
                    # ai_score3 = ai_score3 * 2
                    if player_score3 == 4:
                        player_score3 = 1000
                        ai_score3 = 0
            pos_num4 = 0
            neg_num = 0
            if (row_val+col_val+1==num_cols):
                for i in range(num_cols):

                    if board[i][num_cols-i-1][-1] > 0:
                        player_score4 =player_score4+ board[i][num_cols-i-1][-1]
                        pos_num4 = pos_num4 + 1
                    if board[i][num_cols-i-1][-1] < 0:
                        ai_score4 =ai_score4+ abs(board[i][num_cols-i-1][-1])
                        neg_num = neg_num + 1
                    if pos_num4 == num_cols:
                        result = 'win'
                        break
                    if neg_num == num_cols:
                        result = 'lose'
                        break


                if pos_num4 == 3:
                    # player_score4 = player_score4 * 2

                    if ai_score4 == 4:
                        ai_score4 = 1000
                        player_score4 = 0
                if neg_num == 3:
                    # ai_score4 = ai_score4 * 2

                    if player_score4 == 4:
                        player_score4 = 1000
                        ai_score4 = 0
            player_score=player_score1+player_score2+player_score3+player_score4
            ai_score=ai_score1+ai_score2+ai_score3+ai_score4
            print('scores:                         ',player_score,ai_score)


            print(result)

        def press_g(instance):
            global selected_g
            global initial_opo
            global initial_my
            global turn
            global selected_my
            global selected_opo
            if selected_g==0:
                bu_text=list(instance.ids.keys())[0].split('_')[0]
                bu_side=list(instance.ids.keys())[0].split('_')[-1]
                if grabbing_sfx:
                    grabbing_sfx.volume = 1
                    grabbing_sfx.play()
                if turn == 1:
                    if bu_side=='1':
                        selected_g=initial_my[int(bu_text)-1].pop()
                        st_size=abs(initial_my[int(bu_text) - 1][-1])
                        instance.background_normal =f"resources/gobbs/{gobb_name}_1_{st_size}.png"
                        instance.background_down =f"resources/gobbs/{gobb_name}_1_{st_size}.png"

                        instance.size_hint = dict_size_hint[st_size]
                        initial_my[int(bu_text)-1]=[0]+initial_my[int(bu_text)-1]
                        gobb_my_display.source=f"resources/gobbs/{gobb_name}_1.png"
                        gobb_my_display.size_hint=dict_size_hint[abs(selected_g)]

                if turn == -1:
                    if bu_side=='-1':
                        selected_g=initial_opo[int(bu_text)-1].pop()
                        st_size=abs(initial_opo[int(bu_text) - 1][-1])
                        instance.background_normal =f"resources/gobbs/{gobb_name}_0_{st_size}.png"
                        instance.background_down =f"resources/gobbs/{gobb_name}_0_{st_size}.png"
                        instance.size_hint = dict_size_hint[st_size]
                        initial_opo[int(bu_text)-1]=[0]+initial_opo[int(bu_text)-1]
                        gobb_opo_display.source = f"resources/gobbs/{gobb_name}_0.png"
                        gobb_opo_display.size_hint = dict_size_hint[abs(selected_g)]

                print('g:',selected_g)
                print( 'initial opo:',initial_opo)
                print('initial my:',initial_my)
        def winningpopup_close(self):
            global start
            self.parent.parent.parent.parent.parent.dismiss()
            start=True


        def press_b(instance):
            global selected_g
            global board
            global turn
            global initial_opo
            global initial_my
            global dict_size_hint
            global dict_opo_box
            global dict_board
            global dict_my_box

            tile=list(instance.ids.keys())[0]
            print(tile)

            selected_b=board[int(tile.split(',')[0])][int(tile.split(',')[-1])][-1]
            if selected_g!=0:

                if abs(int(selected_g))>abs(int(selected_b)):
                    stone_put = SoundLoader.load(f'resources/sound effects/stone put{abs(selected_g)}.wav')

                    if stone_put:
                        stone_put.volume = 0.5
                        stone_put.play()
                    t=1
                    if turn==-1:
                        t=0
                        gobb_opo_display.source = "resources/gobbs/empty.png"
                    else:
                        gobb_my_display.source="resources/gobbs/empty.png"
                    instance.background_normal=f"resources/gobbs/{gobb_name}_{str(t)}_{abs(selected_g)}.png"
                    instance.background_down=f"resources/gobbs/{gobb_name}_{str(t)}_{abs(selected_g)}.png"
                    instance.size_hint = dict_size_hint[abs(selected_g)]
                    print(instance.background_normal)
                    board[int(tile.split(',')[0])][int(tile.split(',')[-1])].append(int(selected_g))
                    print(board)
                    print(instance.ids)
                    selected_g=0

                    switch_turn()
                else:
                    if block:
                        block.volume = 0.5
                        block.play()


            else:
                if int(selected_b)!=0:
                    t=1
                    that_b=board[int(tile.split(',')[0])][int(tile.split(',')[-1])]
                    sel=that_b[-2]
                    if sel<0:
                        t=0

                        sel=abs(sel)
                    if that_b[-1]*turn>0:
                        if sel!=0:
                            instance.background_normal = f"resources/gobbs/{gobb_name}_{t}_{abs(sel)}.png"
                            instance.background_down = f"resources/gobbs/{gobb_name}_{t}_{abs(sel)}.png"
                            instance.size_hint = dict_size_hint[abs(sel)]
                            selected_g = board[int(tile.split(',')[0])][int(tile.split(',')[-1])].pop()
                        elif sel==0:
                            instance.background_normal = "resources/gobbs/empty.png"
                            instance.background_down = "resources/gobbs/empty.png"

                            selected_g = board[int(tile.split(',')[0])][int(tile.split(',')[-1])].pop()
                        if turn==1:

                            gobb_my_display.source = f"resources/gobbs/{gobb_name}_1.png"
                            gobb_my_display.size_hint = dict_size_hint[abs(selected_g)]
                        elif turn==-1:

                            gobb_opo_display.source = f"resources/gobbs/{gobb_name}_0.png"
                            gobb_opo_display.size_hint = dict_size_hint[abs(selected_g)]

            check_win(tile=tile,board=board)
            if (result=='win')|(result=='lose'):
                global start
                start = False

                ResultAnalBox=BoxLayout()
                Retry=Button(text='Try Again?', on_press=reset, on_release=winningpopup_close,size_hint=[0.2,0.2])
                BacktoMain=Button(text='Main Menu')
                ResultAnalBox.add_widget(Retry)

                winningpopup = Popup(title='Game ended.',content =BoxLayout(),
                                     # Label(text=f'You {result}!'),
                                     size_hint=(1, 1), size=(400, 400),opacity=0.7)
                winningpopup.content.add_widget(ResultAnalBox)

                winningpopup.open()
        dict_opo_box={}
        opp_box=AnchorLayout(size_hint=[1,0.25])
        b1 = BoxLayout(orientation= 'horizontal',size_hint=[0.95,0.95],pos_hint= {'center_x':0.5, 'center_y':0.5})
        for i in range(len(initial_opo)):
            gob_box = AnchorLayout()
            dict_opo_box[f'{i}'] = Button(on_press=press_g,background_normal= f"resources/gobbs/{gobb_name}_0_4.png",border=(0,0,0,0),size_hint=[0.85,0.85],pos_hint= {'center_x':0.5, 'center_y':0.5},background_down= f"resources/gobbs/{gobb_name}_0_4.png")
            dict_opo_box[f'{i}'].ids[str(i+1)+'_-1'] = dict_opo_box[f'{i}']
            gob_box.add_widget(dict_opo_box[f'{i}'])
            b1.add_widget(gob_box)


        face_box_opo=CircularAnchor()
        face_box_opo.add_widget(Button(background_normal= f"resources/face_varients/18_default_fr_1.png",border=(0,0,0,0),size_hint=[0.95,0.95]))
        b1.add_widget(face_box_opo)
        opp_box.add_widget(b1)


        dict_board={}
        board_box=CustomLayout()
        g1 = GridLayout(cols=num_cols,rows=num_cols+1,size_hint=[0.95,0.95],pos_hint= {'center_x':0.5, 'center_y':0.5})
        for i in range(num_cols):
            for k in range(num_cols):
                tile_box=AnchorLayout()

                dict_board[f'{i},{k}']=Button( on_press=press_b,background_normal= f'resources/{board_name}/empty.png',border=(0,0,0,0),background_down= f'resources/{board_name}/empty.png')
                dict_board[f'{i},{k}'].ids[f'{str(i)},{str(k)}']=dict_board[f'{i},{k}']
                tile_box.add_widget(dict_board[f'{i},{k}'])
                g1.add_widget(tile_box)
        board_box.add_widget(g1)


        dict_my_box={}
        player_box=AnchorLayout(size_hint=[1,0.25])
        b2 = BoxLayout(orientation= 'horizontal',size_hint=[0.95,0.95],pos_hint= {'center_x':0.5, 'center_y':0.5})
        face_box_player=CircularAnchor()
        face_box_player.add_widget(Button(background_normal= f"resources/face_varients/16_default_fr_1.png",border=(0,0,0,0),size_hint=[0.95,0.95]))
        b2.add_widget(face_box_player)
        for i in range(len(initial_my)):
            gob_box = AnchorLayout()
            dict_my_box[f'{i}']=Button(on_press=press_g,background_normal= f"resources/gobbs/{gobb_name}_1_4.png",
                           border=(0,0,0,0),size_hint=[0.85,0.85],pos_hint= {'center_x':0.5, 'center_y':0.5},background_down=f"resources/gobbs/{gobb_name}_1_4.png")
            dict_my_box[f'{i}'].ids[str(i+1)+'_1']=dict_my_box[f'{i}']
            gob_box.add_widget(dict_my_box[f'{i}'])
            b2.add_widget(gob_box)
        player_box.add_widget(b2)


        time_box_opo=TimeFrame(size_hint=[1,0.25])
        global to_time
        to_time=time.time()+30.
        now_time=time.time()
        timeleft=to_time-now_time
        time_wid_opo=Button(size_hint=[(timeleft)/28,0.1],pos_hint= {'left':0, 'center_y':0.1}, border=(0,0,0,0),background_color=[1,1,1,1])
        time_box_opo.add_widget(time_wid_opo)

        time_box_my=TimeFrameMy(size_hint=[1,0.25])
        time_wid_my=Button(size_hint=[(timeleft)/28,0.1],pos_hint= {'left':0, 'center_y':0.9}, border=(0,0,0,0),background_color=[1,1,1,1])
        time_box_my.add_widget(time_wid_my)

        myturnsign=MyLabel(text='Turn',pos_hint={'center_x':0.15, 'center_y':0.2} ,size_hint=[0.4,0.4])
        time_box_my.add_widget(myturnsign)
        yourturnsign = MyLabel(text='Turn', pos_hint={'center_x': 0.85, 'center_y': 0.8}, size_hint=[0.4, 0.4])
        time_box_opo.add_widget(yourturnsign)

        gobb_socket_my=Image(source="resources/gobb_socket/1.png", pos_hint={'center_x': 0.5, 'center_y': 0.4}, size_hint=[0.85, 0.85])
        time_box_my.add_widget(gobb_socket_my)
        gobb_socket_opo=Image(source="resources/gobb_socket/1.png", pos_hint={'center_x': 0.5, 'center_y': 0.6}, size_hint=[0.85, 0.85])
        time_box_opo.add_widget(gobb_socket_opo)

        gobb_my_display = Image(source="resources/gobbs/empty.png", pos_hint={'center_x': 0.5, 'center_y': 0.4},
                               size_hint=[0.85, 0.85])
        time_box_my.add_widget(gobb_my_display)
        gobb_opo_display = Image(source="resources/gobbs/empty.png", pos_hint={'center_x': 0.5, 'center_y': 0.6},
                                size_hint=[0.85, 0.85])
        time_box_opo.add_widget(gobb_opo_display)


        self.add_widget(opp_box)
        self.add_widget(time_box_opo)
        self.add_widget(board_box)
        self.add_widget(time_box_my)
        self.add_widget(player_box)



TheLabApp().run()


