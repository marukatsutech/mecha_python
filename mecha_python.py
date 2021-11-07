# Mecha.Python
import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.patches as patches
import numpy as np


def arm_right(ax, x, y, s):
    th_deg = - 80
    th = th_deg / 180 * np.pi
    ln = s * 1.1
    shoulder_pnt_x = x + s * 0.8
    shoulder_pnt_y = y - s * 0.9
    hand_pnt_x = shoulder_pnt_x + ln * np.cos(th)
    hand_pnt_y = shoulder_pnt_y + ln * np.sin(th)
    arm_pnt_x = shoulder_pnt_x + ln * 0.9 * np.cos(th)
    arm_pnt_y = shoulder_pnt_y + ln * 0.9 * np.sin(th)
    arm_r, = ax.plot([shoulder_pnt_x, arm_pnt_x], [shoulder_pnt_y, arm_pnt_y], linestyle=':', c='yellow',
                     linewidth=2)
    hand_r = patches.Wedge(center=(hand_pnt_x, hand_pnt_y), r=s * 0.25, width=s * 0.2, theta1=th_deg + 30,
                           theta2=th_deg + 330, fc='yellow', ec='darkgray')
    ax.add_patch(hand_r)
    shoulder_r = patches.Circle(xy=(shoulder_pnt_x, shoulder_pnt_y), radius=s * 0.2, fc='yellow', ec='darkgray')
    ax.add_patch(shoulder_r)


def arm_left(ax, x, y, s):
    arm_l, = ax.plot([x - s * 0.8, x - s * 1 * 0.95], [y - s * 0.9, y - s * 2 * 0.9], linestyle=':', c='#3673a5',
                     linewidth=2)
    hand_l = patches.Wedge(center=(x - s * 1, y - s * 2), r=s * 0.25, width=s * 0.2, theta1=-60, theta2=240, fc='#3673a5',
                           ec='darkgray')
    ax.add_patch(hand_l)
    shoulder_l = patches.Circle(xy=(x - s * 0.8, y - s * 0.9), radius=s * 0.2, fc='#3673a5', ec='darkgray')
    ax.add_patch(shoulder_l)


def head(ax, x, y, s):
    antenna_c, = ax.plot([x, x], [y + s * 0.5, y + s * 1.2], linestyle='-', c='gray',
                         linewidth=1)
    antenna_r, = ax.plot([x, x + s * 0.2], [y + s * 0.65, y + s * 0.85], linestyle='-', c='gray',
                         linewidth=1)
    antenna_l, = ax.plot([x, x - s * 0.2], [y + s * 0.65, y + s * 0.85], linestyle='-', c='gray',
                         linewidth=1)
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
    hd = patches.Rectangle(xy=(x - s * 2 / 2, y - s * 1 / 2), width=s * 2, height=s * 1, fc='lightgray',
                             ec='darkgray')
    ax.add_patch(hd)
    eye_r = patches.Circle(xy=(x + s * 0.5, y + s * 0.1), radius=s * 0.25, fc='yellow', ec='orange')
    ax.add_patch(eye_r)
    eye_l = patches.Circle(xy=(x - s * 0.5, y + s * 0.1), radius=s * 0.25, fc='yellow', ec='orange')
    ax.add_patch(eye_l)
    mouse = patches.Rectangle(xy=(x - s * 0.4 / 2, y - s * 0.3), width=s * 0.4, height=s * 0.05, fc='dimgray',
                             ec='dimgray')
    ax.add_patch(mouse)


def robot(ax, x, y, s):
    leg_r, = ax.plot([x + s * 0.4, x + s * 0.4], [y - s * 2, y - s * 3 * 0.9], linestyle=':', c='lightgray',
                     linewidth=2)
    leg_l, = ax.plot([x - s * 0.4, x - s * 0.4], [y - s * 2, y - s * 3 * 0.9], linestyle=':', c='lightgray',
                     linewidth=2)
    foot_r = patches.Wedge(center=(x + s * 0.4, y - s * 3), r=0.15, theta1=0, theta2=180, fc='lightgray',
                           ec='darkgray')
    ax.add_patch(foot_r)
    foot_l = patches.Wedge(center=(x - s * 0.4, y - s * 3), r=0.15, theta1=0, theta2=180, fc='lightgray',
                           ec='darkgray')
    ax.add_patch(foot_l)
    body = patches.Rectangle(xy=(x - s * 1 / 2, y - s * 1.9), width=s * 1, height=s * 1.2, fc='lightgray',
                             ec='darkgray')
    ax.add_patch(body)
    dsp = patches.Rectangle(xy=(x - s * 0.8 / 2, y - s * 1.4), width=s * 0.8, height=s * 0.6, fc='white',
                             ec='darkgray')
    ax.add_patch(dsp)
    tx_dsp = ax.text(x, y - s * 1.2, 'Py',horizontalalignment="center", c='darkgray')
    head(ax, x, y, s)
    arm_right(ax, x, y, s)
    arm_left(ax, x, y, s)


def back():
    pass


def play_pause():
    pass


def forward():
    pass


def update(f):
    global cnt, tx_cnt
    # Update items
    # Count
    tx_cnt.set_text(" cnt=" + str(cnt))
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
fig = Figure(figsize=(8, 4), facecolor="lightgray" )
ax1 = fig.add_subplot(111)
ax1.set_xlim(x_min, x_max)
ax1.set_ylim(y_min, y_max)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_title('Mecha.Python', c='dimgray')
ax1.set_aspect('equal')
ax1.set_facecolor('#002000')

# Generate items Note;  The variables of some items need ',' to use set parameters.
tx_cnt = ax1.text(x_min, y_max * 0.95, 'cnt=' + str(0), c='lime')
robot(ax1, 4., 2., 0.5)

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
btn_back = tkinter.Button(root, text="Back", command=back)
btn_back.pack(side='left')
btn_play_pause = tkinter.Button(root, text="Play/Pause", command=play_pause)
btn_play_pause.pack(side='left')
btn_forward = tkinter.Button(root, text="Forward", command=forward)
btn_forward.pack(side='left')

# main loop
tkinter.mainloop()
