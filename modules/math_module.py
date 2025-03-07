import matplotlib.pyplot as plt
import numpy as np


# [length_of_cycle, duration_green, intergreen_cycle, yellow_red_duration, yellow_duration]

def calculate(values):
    k_duration = values[0] / 2  # duration of cycle for one light
    k_short_red = values[2] - values[4]  # duration of red between yellows
    k_long_red = values[1] + values[2] - values[3]  # duration of red during kull K cycle
    values.extend([k_duration, k_short_red, k_long_red])
    if all(value > 0 for value in values):
        draw_method_choice(values)
    else:
        print("theres problem here")


def draw_method_choice(values):
    inpt = int(input("enter 1 for color, 2 for black and white: \n"))
    if inpt == 1 or inpt == 2:
        values.append(inpt)
        draw(values)
    else:
        print("wrong input")


# [length_of_cycle (0), duration_green (1), intergreen_cycle (2), yellow_red_duration (3),yellow_duration (4), k_duration (5), k_short_red (6), k_long_red (7), color (8)]
def draw(values):
    fig, ax = plt.subplots(figsize=(170 * 0.0393700787, 100 * 0.0393700787))  # 150mm x 120mm
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    fig.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

    barheight = 20 * 0.0393700787  # 2mm to inches
    for i, start_time in zip([1, 0], [0, values[5]]):  # from 0 to the half of the cycle K1, o=fron half of the cycle K2
        y_axis = i
        # draw green light
        ax.barh(y_axis, values[1], left=start_time, height=barheight, color='green', edgecolor='black')
        # draw yellow light
        ax.barh(y_axis, values[4], left=start_time + values[1], height=barheight, color='yellow', edgecolor='black')
        # draw intergreen red
        ax.barh(y_axis, values[6], left=start_time + values[1] + values[4], height=barheight, color='red',
                edgecolor='black')
        # draw long red and red-yellow one
        if start_time == 0:
            ax.barh(y_axis, values[7], height=barheight, left=start_time + values[5], color='red', edgecolor='black')
            ax.barh(y_axis, values[3], height=barheight, left=start_time + values[5] + values[7], color='orange',
                    edgecolor='black')
        elif start_time == values[5]:
            ax.barh(y_axis, values[7], height=barheight, left=start_time - values[5], color='red', edgecolor='black')
            ax.barh(y_axis, values[3], height=barheight, left=start_time - values[3], color='orange', edgecolor='black')

    ax.set_yticks([0,1])
    ax.set_yticklabels(["K 1", "K 2"])
    ax.tick_params(axis="y", length=0)
    ax.set_xticks(np.arange(0, values[0] + 1, 1))  # Skala co sekundę
    ax.set_xlim(0, values[0])
    ax.set_xlabel("")
    ax.tick_params(axis="x", labelsize=8)
    def custom_xtick(x, pos):
        if x % 5 == 0:
            return f'{int(x)}'
        else:
            return ''
    ax.xaxis.set_major_formatter(plt.FuncFormatter(custom_xtick))
    plt.tight_layout()
    ax.set_axisbelow(True)
    ax.set_title("")
    ax.grid(axis="x", linestyle="--", alpha=0.7, linewidth=0.5)

    plt.show()
