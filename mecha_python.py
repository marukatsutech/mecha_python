# Mecha.Python
import tkinter
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.patches as patches
import numpy as np
import pandas as pd


def arm_right(ax, x, y, s, th_deg):
    th = th_deg / 180 * np.pi
    ln = s * 1.1
    shoulder_pnt_x = x + s * 0.8
    shoulder_pnt_y = y - s * 0.9
    hand_pnt_x = shoulder_pnt_x + ln * np.cos(th)
    hand_pnt_y = shoulder_pnt_y + ln * np.sin(th)
    arm_pnt_x = shoulder_pnt_x + ln * 0.9 * np.cos(th)
    arm_pnt_y = shoulder_pnt_y + ln * 0.9 * np.sin(th)
    ax.plot([shoulder_pnt_x, arm_pnt_x], [shoulder_pnt_y, arm_pnt_y], linestyle=':', c='yellow', linewidth=2)
    hand_r = patches.Wedge(center=(hand_pnt_x, hand_pnt_y), r=s * 0.25, width=s * 0.2, theta1=th_deg + 30,
                           theta2=th_deg + 330, fc='yellow', ec='darkgray')
    ax.add_patch(hand_r)
    shoulder_r = patches.Circle(xy=(shoulder_pnt_x, shoulder_pnt_y), radius=s * 0.2, fc='yellow', ec='darkgray')
    ax.add_patch(shoulder_r)


def arm_left(ax, x, y, s, th_deg):
    th = th_deg / 180 * np.pi
    ln = s * 1.1
    shoulder_pnt_x = x - s * 0.8
    shoulder_pnt_y = y - s * 0.9
    hand_pnt_x = shoulder_pnt_x + ln * np.cos(th)
    hand_pnt_y = shoulder_pnt_y + ln * np.sin(th)
    arm_pnt_x = shoulder_pnt_x + ln * 0.9 * np.cos(th)
    arm_pnt_y = shoulder_pnt_y + ln * 0.9 * np.sin(th)
    ax.plot([shoulder_pnt_x, arm_pnt_x], [shoulder_pnt_y, arm_pnt_y], linestyle=':', c='#3673a5', linewidth=2)
    hand_l = patches.Wedge(center=(hand_pnt_x, hand_pnt_y), r=s * 0.25, width=s * 0.2, theta1=th_deg + 30,
                           theta2=th_deg + 330, fc='#3673a5', ec='darkgray')
    ax.add_patch(hand_l)
    shoulder_l = patches.Circle(xy=(shoulder_pnt_x, shoulder_pnt_y), radius=s * 0.2, fc='#3673a5', ec='darkgray')
    ax.add_patch(shoulder_l)


def head(ax, x, y, s):
    ax.plot([x, x], [y + s * 0.5, y + s * 1.2], linestyle='-', c='gray', linewidth=1)
    ax.plot([x, x + s * 0.2], [y + s * 0.65, y + s * 0.85], linestyle='-', c='gray', linewidth=1)
    ax.plot([x, x - s * 0.2], [y + s * 0.65, y + s * 0.85], linestyle='-', c='gray', linewidth=1)
    antenna_p = patches.Circle(xy=(x + s * 0.1, y + s * 1.05), radius=s * 0.1, fill=False, ec='gray')
    ax.add_patch(antenna_p)
    ear_r = patches.FancyArrow(x + s * 1.1, y, s * 0.05, 0, width=s * 0.2, length_includes_head=False,
                               head_width=s * 0.5, head_length=s * 0.3, shape='full', overhang=0,
                               head_starts_at_zero=False, fc='#3673a5', ec='darkgray')
    ax.add_patch(ear_r)
    ear_l = patches.FancyArrow(x - s * 1.1, y, - s * 0.05, 0, width=s * 0.2, length_includes_head=False,
                               head_width=s * 0.5, head_length=s * 0.3, shape='full', overhang=0,
                               head_starts_at_zero=False, fc='yellow', ec='darkgray')
    ax.add_patch(ear_l)
    hd = patches.Rectangle(xy=(x - s * 2 / 2, y - s * 1 / 2), width=s * 2, height=s * 1, fc='lightgray', ec='darkgray')
    ax.add_patch(hd)
    eye_r = patches.Circle(xy=(x + s * 0.5, y + s * 0.1), radius=s * 0.25, fc=eyes_color, ec='orange')
    ax.add_patch(eye_r)
    eye_l = patches.Circle(xy=(x - s * 0.5, y + s * 0.1), radius=s * 0.25, fc=eyes_color, ec='orange')
    ax.add_patch(eye_l)
    mouse = patches.Rectangle(xy=(x - s * 0.4 / 2, y - s * 0.3), width=s * 0.4, height=s * 0.05,
                              fc='dimgray', ec='dimgray')
    ax.add_patch(mouse)


def robot(ax, x, y, s):
    ax.plot([x + s * 0.4, x + s * 0.4], [y - s * 1.5, y - s * 3 * 0.9], linestyle=':', c='lightgray', linewidth=2)
    ax.plot([x - s * 0.4, x - s * 0.4], [y - s * 1.5, y - s * 3 * 0.9], linestyle=':', c='lightgray', linewidth=2)
    foot_r = patches.Wedge(center=(x + s * 0.4, y - s * 3), r=s * 0.3, theta1=0, theta2=180,
                           fc='lightgray', ec='darkgray')
    ax.add_patch(foot_r)
    foot_l = patches.Wedge(center=(x - s * 0.4, y - s * 3), r=s * 0.3, theta1=0, theta2=180,
                           fc='lightgray', ec='darkgray')
    ax.add_patch(foot_l)
    body = patches.Rectangle(xy=(x - s * 1 / 2, y - s * 1.9), width=s * 1, height=s * 1.2,
                             fc='lightgray', ec='darkgray')
    ax.add_patch(body)
    dsp = patches.Rectangle(xy=(x - s * 0.8 / 2, y - s * 1.4), width=s * 0.8, height=s * 0.6, fc='white',
                            ec='darkgray')
    ax.add_patch(dsp)
    ax.text(x, y - s * 1.2, dsp_txt, horizontalalignment="center", c='darkgray', size=s * font_size * 2.5)
    head(ax, x, y, s)
    arm_right(ax, x, y, s, arm_th_deg_r)
    arm_left(ax, x, y, s, arm_th_deg_l)


def balloon_up():
    global balloon_up_txt
    points = [[x_min + 0.5, y_max - 0.3], [x_max - 0.5, y_max - 0.3], [x_max - 0.5, y_max - 1],
              [(x_max - x_min) / 2 + 0.1, y_max - 1], [(x_max - x_min) / 2, y_max - 1.2],
              [(x_max - x_min) / 2 - 0.1, y_max - 1], [x_min + 0.5, y_max - 1]]
    patch = patches.Polygon(xy=points, closed=True, fill=False, ec='lime', linewidth=1)
    ax1.add_patch(patch)
    ax1.text((x_max - x_min) / 2, y_max - 0.35, balloon_up_txt, horizontalalignment="center",
             verticalalignment="top", c='lime', size=font_size)


def balloon_right():
    global balloon_right_txt
    points = [[x_min + 2, y_min + 0.3], [x_max - 0.3, y_min + 0.3], [x_max - 0.3, y_min + 1],
              [x_min + 2, y_min + 1], [x_min + 2, y_min + 0.9], [x_min + 1.8, y_min + 1.2],
              [x_min + 2, y_min + 0.7]]
    patch = patches.Polygon(xy=points, closed=True, fill=False, ec='lime', linewidth=1)
    ax1.add_patch(patch)
    ax1.text(x_min + 2.1, y_min + 0.95, balloon_right_txt, c='lime', verticalalignment="top", size=font_size)


def board():
    global board_txt
    points = [[x_min + 2, y_min + 1.2], [x_max - 0.3, y_min + 1.2], [x_max - 0.3, y_max - 0.3],
              [x_min + 2, y_max - 0.3], [x_min + 2, y_min + 1.2]]
    patch = patches.Polygon(xy=points, closed=True, fill=False, ec='green', linewidth=1)
    ax1.add_patch(patch)
    ax1.text(x_min + 2.1, y_max - 0.35, board_txt, c='lime', verticalalignment="top", size=font_size)


def load_file():
    global file_name, balloon_right_txt, df
    file_name = ent_file.get() + ".csv"
    try:
        df = pd.read_csv(file_name, sep=',', index_col=0)
        print(file_name)
        print(df.head(3))
        print(df.tail(3))
    except Exception as e:
        print(e)
        balloon_right_txt = str(e) + "\nPut a file in the same directory of mecha_python.py"
        presentation()


def left():
    global x_robot
    x_robot = x_left


def center():
    global x_robot
    x_robot = x_center


def right():
    global x_robot
    x_robot = x_right


def raise_hand_r():
    global arm_th_deg_r, on_bye
    on_bye = False
    arm_th_deg_r = 80.


def raise_hand_l():
    global on_bye, arm_th_deg_l
    on_bye = False
    arm_th_deg_l = 100.


def lower_hand_r():
    global on_bye, arm_th_deg_r
    on_bye = False
    arm_th_deg_r = arm_th_deg_r_default


def lower_hand_l():
    global on_bye, arm_th_deg_l
    on_bye = False
    arm_th_deg_l = arm_th_deg_l_default


def pointing():
    global arm_th_deg_r, on_bye
    on_bye = False
    arm_th_deg_r = 30.


def reset():
    global on_bye, on_balloon_up, on_balloon_right, on_board, dsp_txt
    on_bye = False
    lower_hand_r()
    lower_hand_l()
    dsp_txt = "Py"


def bye():
    global on_bye, dsp_txt
    reset()
    on_bye = True
    dsp_txt = "Bye"


def hi():
    global on_bye, on_balloon_up, x_robot, dsp_txt
    reset()
    raise_hand_l()
    dsp_txt = "Hi!"


def ok():
    global on_bye, on_balloon_up, x_robot, dsp_txt
    raise_hand_r()
    raise_hand_l()
    dsp_txt = "Ok!"


def eyes_col(col):
    global eyes_color
    if col == "yellow":
        eyes_color = "yellow"
    elif col == "gray":
        eyes_color = "gray"
    elif col == "red":
        eyes_color = "red"
    else:
        eyes_color = "yellow"


def greet():
    global on_balloon_up, on_balloon_right, on_board, x_robot
    reset()
    x_robot = x_center
    on_balloon_up = True
    on_balloon_right = False
    on_board = False


def presentation():
    global on_balloon_up, on_balloon_right, on_board, x_robot
    reset()
    x_robot = x_left
    on_balloon_up = False
    on_balloon_right = True
    on_board = True


def hide():
    global on_balloon_up, on_balloon_right, on_board
    on_balloon_up = False
    on_balloon_right = False
    on_board = False


def show_ticks():
    global ticks_on
    ticks_on = True


def hide_ticks():
    global ticks_on
    ticks_on = False


def show_grid():
    global grid_on
    grid_on = True


def hide_grid():
    global grid_on
    grid_on = False


def show_back_anime():
    global back_anime_on
    back_anime_on = True


def hide_back_anime():
    global back_anime_on
    back_anime_on = False


def back_ground_animation(cyc):
    y = np.sin(x_back - cyc) + (y_max - y_min) / 2.
    ax1.plot(x_back, y)


def play():
    global is_play
    is_play = True


def pause():
    global is_play
    is_play = False


def replay():
    global is_play, is_end, sequence_num, cnt, ticks_on, grid_on, back_anime_on
    is_end = False
    sequence_num = 0
    cnt = 0
    is_play = True
    ticks_on = False
    grid_on = False
    back_anime_on = False


def exe_command():
    global df, sequence_num, is_end, is_play, title, balloon_up_txt, balloon_right_txt, board_txt, wait_cnt
    if is_play:
        if wait_cnt == 0:
            if not is_end:
                sequence_num += 1
                cmd = df.at[sequence_num, 'command']
                opd = df.at[sequence_num, 'operand']
                print(str(cmd) + ': ' + str(opd))
                if cmd == "pause":
                    is_play = False
                elif cmd == "EOF":
                    is_end = True
                elif cmd == "title_clear":
                    title = ""
                elif cmd == "title":
                    title = str(opd).strip('"')
                elif cmd == "balloon_up_clear":
                    balloon_up_txt = ""
                elif cmd == "balloon_up":
                    balloon_up_txt = str(opd).strip('"')
                elif cmd == "balloon_up_append":
                    balloon_up_txt = balloon_up_txt + "\n"
                    if str(opd) != "nan":
                        balloon_up_txt = balloon_up_txt + str(opd).strip('"')
                elif cmd == "board_clear":
                    board_txt = ""
                elif cmd == "board":
                    board_txt = str(opd).strip('"')
                elif cmd == "board_append":
                    board_txt = board_txt + "\n"
                    if str(opd) != "nan":
                        board_txt = board_txt + str(opd).strip('"')
                elif cmd == "balloon_right_clear":
                    balloon_right_txt = ""
                elif cmd == "balloon_right":
                    balloon_right_txt = str(opd).strip('"')
                elif cmd == "balloon_right_append":
                    balloon_right_txt = balloon_right_txt + "\n"
                    if str(opd) != "nan":
                        balloon_right_txt = balloon_right_txt + str(opd).strip('"')
                elif cmd == "hi":
                    hi()
                elif cmd == "ok":
                    ok()
                elif cmd == "bye":
                    bye()
                elif cmd == "reset":
                    reset()
                elif cmd == "greet":
                    greet()
                elif cmd == "presentation":
                    presentation()
                elif cmd == "hide":
                    hide()
                elif cmd == "eyes_color":
                    eyes_col(str(opd).strip('"'))
                elif cmd == "pointing":
                    pointing()
                elif cmd == "show_ticks":
                    show_ticks()
                elif cmd == "hide_ticks":
                    show_ticks()
                elif cmd == "show_grid":
                    show_grid()
                elif cmd == "hide_grid":
                    hide_grid()
                elif cmd == "show_back_anime":
                    show_back_anime()
                elif cmd == "hide_back_anime":
                    hide_back_anime()
                elif cmd == "wait":
                    wait_cnt = int(opd)
        else:
            wait_cnt -= 1


def bye_motion():
    global motion_cnt, arm_th_deg_r
    if on_bye:
        if motion_cnt == 0:
            arm_th_deg_r = 60
        elif motion_cnt == 1:
            arm_th_deg_r = 75
        elif motion_cnt == 2:
            arm_th_deg_r = 90
        elif motion_cnt == 3:
            arm_th_deg_r = 75
        elif motion_cnt == 4:
            arm_th_deg_r = 75
        motion_cnt += 1
        if motion_cnt > 4:
            motion_cnt = 0


def set_axis():
    ax1.set_xlim(x_min, x_max)
    ax1.set_ylim(y_min, y_max)
    if not ticks_on:
        ax1.set_xticks([])
        ax1.set_yticks([])
    if grid_on:
        ax1.grid()
    ax1.set_title(title, c='dimgray')
    ax1.set_aspect('equal')
    ax1.set_facecolor('#002000')


def update(f):
    global cnt, font_size
    ax1.cla()
    set_axis()
    # Update items
    if back_anime_on:
        back_ground_animation(f)
    ax1.text(x_min, y_max * 0.95, ' file:' + file_name + ' cnt=' + str(cnt), c='lime', size=font_size)
    bye_motion()
    robot(ax1, x_robot, y_robot, s_robot)
    # Speech balloon up
    if on_balloon_up:
        balloon_up()
    # Speech balloon right
    if on_balloon_right:
        balloon_right()
    # Board
    if on_board:
        board()

    exe_command()
    if is_play:
        cnt += 1

    screen_height = root.winfo_height()
    font_size = int((y_max - y_min) * 2.6) * screen_height / 565


# Global variables
x_min = 0.
x_max = 8.
y_min = 0.
y_max = 4.

cnt = 0
is_play = False
sequence_num = 0
is_end = False
ticks_on = False
grid_on = False
back_anime_on = False

x_center = 4.
y_center = 2.
x_left = 1.
x_right = 7.
x_robot = x_center
y_robot = y_center
s_robot = 0.5     # Scale
font_size = int((y_max - y_min) * 2.6)

arm_th_deg_r_default = - 80
arm_th_deg_l_default = - 100
arm_th_deg_r = arm_th_deg_r_default
arm_th_deg_l = arm_th_deg_l_default

eyes_color = "yellow"

on_bye = False
on_balloon_up = False
on_balloon_right = False
on_board = False

motion_cnt = 0
wait_cnt = 0

dsp_txt = "Py"
hello_txt = "Hello world.\nI am Mecha.Python!"
balloon_up_txt = hello_txt
balloon_right_txt = "I will start my presentation."
board_txt = "STEP 1"
file_name = ""

title_default = "Mecha.Python"
title = title_default

# For back ground animation
x_back = np.linspace(0, 10, 200)

# Create dataset
dummy = pd.Series(list('abc'))
# Create dummy variables
df = pd.get_dummies(dummy)

# Generate tkinter
root = tkinter.Tk()
root.title("Mecha.Python")

# Generate figure and axes
fig = Figure(facecolor="lightgray")
ax1 = fig.add_subplot(111)
set_axis()

# Embed a figure in canvas
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')

# Animation
anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)

# Tkinter widgets

# Toolbar
toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

# Button
btn_back = tkinter.Button(root, text="Left", command=left)
btn_back.pack(side='left')
btn_play_pause = tkinter.Button(root, text="Center", command=center)
btn_play_pause.pack(side='left')
btn_forward = tkinter.Button(root, text="Right", command=right)
btn_forward.pack(side='left')

btn_raise_hand_l = tkinter.Button(root, text="Raise L", command=raise_hand_l)
btn_raise_hand_l.pack(side='left')
btn_raise_hand_r = tkinter.Button(root, text="Raise R", command=raise_hand_r)
btn_raise_hand_r.pack(side='left')
btn_lower_hand_l = tkinter.Button(root, text="Lower L", command=lower_hand_l)
btn_lower_hand_l.pack(side='left')
btn_lower_hand_r = tkinter.Button(root, text="Lower R", command=lower_hand_r)
btn_lower_hand_r.pack(side='left')

btn_hi = tkinter.Button(root, text="Hi!", command=hi)
btn_hi.pack(side='left')
btn_ok = tkinter.Button(root, text="Ok!", command=ok)
btn_ok.pack(side='left')
btn_bye = tkinter.Button(root, text="Bye!", command=bye)
btn_bye.pack(side='left')
btn_reset = tkinter.Button(root, text="Reset", command=reset)
btn_reset.pack(side='left')

btn_greet = tkinter.Button(root, text="Greet", command=greet)
btn_greet.pack(side='left')
btn_speech = tkinter.Button(root, text="Present", command=presentation)
btn_speech.pack(side='left')
btn_hide_balloons = tkinter.Button(root, text="Hide", command=hide)
btn_hide_balloons.pack(side='left')

# Operation of presentation
frm_ent = ttk.Labelframe(root, relief="ridge", text="Presentation file", labelanchor="n")
frm_ent.pack(side='left')
ent_file = tkinter.Entry(frm_ent)
ent_file.pack(side='left')
btn_load = tkinter.Button(frm_ent, text="Load", command=load_file)
btn_load.pack(side='left')
btn_play = tkinter.Button(frm_ent, text="Play", command=play)
btn_play.pack(side='left')
btn_pause = tkinter.Button(frm_ent, text="Pause", command=pause)
btn_pause.pack(side='left')
btn_replay = tkinter.Button(frm_ent, text="replay", command=replay)
btn_replay.pack(side='left')

# main loop
tkinter.mainloop()
