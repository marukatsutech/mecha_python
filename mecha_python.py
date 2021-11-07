# Mecha.Python
import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.patches as patches
import numpy as np


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
    eye_r = patches.Circle(xy=(x + s * 0.5, y + s * 0.1), radius=s * 0.25, fc='yellow', ec='orange')
    ax.add_patch(eye_r)
    eye_l = patches.Circle(xy=(x - s * 0.5, y + s * 0.1), radius=s * 0.25, fc='yellow', ec='orange')
    ax.add_patch(eye_l)
    mouse = patches.Rectangle(xy=(x - s * 0.4 / 2, y - s * 0.3), width=s * 0.4, height=s * 0.05,
                              fc='dimgray', ec='dimgray')
    ax.add_patch(mouse)


def robot(ax, x, y, s):
    ax.plot([x + s * 0.4, x + s * 0.4], [y - s * 2, y - s * 3 * 0.9], linestyle=':', c='lightgray', linewidth=2)
    ax.plot([x - s * 0.4, x - s * 0.4], [y - s * 2, y - s * 3 * 0.9], linestyle=':', c='lightgray', linewidth=2)
    foot_r = patches.Wedge(center=(x + s * 0.4, y - s * 3), r=0.15, theta1=0, theta2=180, fc='lightgray', ec='darkgray')
    ax.add_patch(foot_r)
    foot_l = patches.Wedge(center=(x - s * 0.4, y - s * 3), r=0.15, theta1=0, theta2=180, fc='lightgray', ec='darkgray')
    ax.add_patch(foot_l)
    body = patches.Rectangle(xy=(x - s * 1 / 2, y - s * 1.9), width=s * 1, height=s * 1.2, fc='lightgray', ec='darkgray')
    ax.add_patch(body)
    dsp = patches.Rectangle(xy=(x - s * 0.8 / 2, y - s * 1.4), width=s * 0.8, height=s * 0.6, fc='white', ec='darkgray')
    ax.add_patch(dsp)
    ax.text(x, y - s * 1.2, dsp_txt, horizontalalignment="center", c='darkgray')
    head(ax, x, y, s)
    arm_right(ax, x, y, s, arm_th_deg_r)
    arm_left(ax, x, y, s, arm_th_deg_l)


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
    global arm_th_deg_l, on_bye
    on_bye = False
    arm_th_deg_l = 100.


def lower_hand_r():
    global arm_th_deg_r, on_bye
    on_bye = False
    arm_th_deg_r = arm_th_deg_r_default


def lower_hand_l():
    global arm_th_deg_l, on_bye
    on_bye = False
    arm_th_deg_l = arm_th_deg_l_default


def bye():
    global on_bye, dsp_txt
    on_bye = True
    dsp_txt = "Bye"


def hi():
    global on_bye, dsp_txt
    on_bye = False
    raise_hand_l()
    dsp_txt = "Hi!"


def reset():
    global on_bye, dsp_txt
    on_bye = False
    lower_hand_r()
    lower_hand_l()
    dsp_txt = "Py"


def set_axis():
    ax1.set_xlim(x_min, x_max)
    ax1.set_ylim(y_min, y_max)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_title('Mecha.Python', c='dimgray')
    ax1.set_aspect('equal')
    ax1.set_facecolor('#002000')


def update(f):
    global cnt, motion_cnt, arm_th_deg_r
    ax1.cla()
    set_axis()
    # Update items
    # Count
    ax1.text(x_min, y_max * 0.95, 'cnt=' + str(cnt), c='lime')
    # Robot
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
    robot(ax1, x_robot, y_robot, s_robot)

    cnt += 1


# Global variables
x_min = 0.
x_max = 8.
y_min = 0.
y_max = 4.

cnt = 0
isPlay = False

# Generate tkinter
root = tkinter.Tk()
root.title("Mecha.Python")

# Generate figure and axes
fig = Figure(figsize=(8, 4), facecolor="lightgray")
ax1 = fig.add_subplot(111)
set_axis()

# Parameters
x_center = 4.
y_center = 2.
x_left = 1.
x_right = 7.
x_robot = x_center
y_robot = y_center
s_robot = 0.5     # Scale
arm_th_deg_r_default = - 80
arm_th_deg_l_default = - 100
arm_th_deg_r = arm_th_deg_r_default
arm_th_deg_l = arm_th_deg_l_default
on_bye = False
motion_cnt = 0
dsp_txt = "Py"

# Embed a figure in canvas
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack()

# Animation
anim = animation.FuncAnimation(fig, update, interval=100)

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
btn_raise_hand_l = tkinter.Button(root, text="Raise L-hand", command=raise_hand_l)
btn_raise_hand_l.pack(side='left')
btn_raise_hand_r = tkinter.Button(root, text="Raise R-hand", command=raise_hand_r)
btn_raise_hand_r.pack(side='left')
btn_lower_hand_l = tkinter.Button(root, text="Lower L-hand", command=lower_hand_l)
btn_lower_hand_l.pack(side='left')
btn_lower_hand_r = tkinter.Button(root, text="Lower R-hand", command=lower_hand_r)
btn_lower_hand_r.pack(side='left')
btn_hi = tkinter.Button(root, text="Hi!", command=hi)
btn_hi.pack(side='left')
btn_bye = tkinter.Button(root, text="Bye!", command=bye)
btn_bye.pack(side='left')
btn_reset = tkinter.Button(root, text="Reset", command=reset)
btn_reset.pack(side='left')


# main loop
tkinter.mainloop()