import matplotlib.pyplot as plt
import numpy as np


def draw_method_choice(values):
    inpt = 1  # int(input("enter 1 for color, 2 for black and white: \n"))
    if inpt == 1 or inpt == 2:
        values.append(inpt)
        draw(values)
    else:
        print("wrong input")


# [length_of_cycle (0), duration_green (1), intergreen_cycle (2), yellow_red_duration (3),yellow_duration (4),
# k_duration (5), k_short_red (6), k_long_red (7), color (8)]
def draw(values):
    fig, ax = plt.subplots(figsize=(250 * 0.0393700787, 100 * 0.0393700787))  # 150mm x 120mm
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    #fig.subplots_adjust(left=0.05, right=0.15, top=0.95, bottom=0.05)

    barheight = 15 * 0.0393700787  # 2mm to inches
    for i, start_time in zip([1, 0], [0, values[5]]):  # from 0 to the half of the cycle K1, from half of the cycle K2
        y_axis = i
        # draw green light
        ax.barh(y_axis, values[1], left=start_time, height=barheight, color='green', edgecolor='black')
        ax.text(start_time + values[1] / 2, y_axis + barheight / 2, f'{values[1]}s', ha='center', va='bottom',
                color='black')
        # draw yellow light
        ax.barh(y_axis, values[4], left=start_time + values[1], height=barheight, color='yellow', edgecolor='black')
        ax.text(start_time + values[1] + values[4] / 2, y_axis + barheight / 2, f'{values[4]}s', ha='center', va='bottom',
                color='black')
        # draw intergreen red
        ax.barh(y_axis, values[6], left=start_time + values[1] + values[4], height=barheight, color='red',
                edgecolor='black')
        ax.text(start_time + values[1] + values[4] + values[6] / 2, y_axis + barheight / 2, f'{values[6]}s', ha='center',
                va='bottom',color='black')
        # draw long red and red-yellow one
        if start_time == 0:
            ax.barh(y_axis, values[7], height=barheight, left=start_time + values[5], color='red', edgecolor='black')
            ax.text(start_time + values[5] + values[7] / 2, y_axis + barheight / 2, f'{values[7]}s', ha='center',
                    va='bottom', color='black')
            ax.barh(y_axis, values[3], height=barheight, left=start_time + values[5] + values[7], color='orange',
                    edgecolor='black')
            ax.text(start_time + values[5] + values[7] + values[3] / 2, y_axis + barheight / 2, f'{values[3]}s', ha='center',
                    va='bottom', color='black')
        elif start_time == values[5]:
            ax.barh(y_axis, values[7], height=barheight, left=start_time - values[5], color='red', edgecolor='black')
            ax.text(start_time - values[5] + values[7] / 2, y_axis + barheight / 2, f'{values[7]}s', ha='center',
                    va='bottom', color='black')
            ax.barh(y_axis, values[3], height=barheight, left=start_time - values[3], color='orange', edgecolor='black')
            ax.text(start_time - values[3] + values[3] / 2, y_axis + barheight / 2, f'{values[3]}s', ha='center', va='bottom',
                    color='black')

    ax.set_yticks([0, 1])
    ax.set_yticklabels(["K 2", "K 1"])
    ax.tick_params(axis="y", length=0)
    ax.set_xticks(np.arange(0, values[0] + 1, 1))  # Skala co sekundę
    ax.set_xlim(0, values[0])
    ax.set_xlabel("")
    ax.tick_params(axis="x", labelsize=8)

    def custom_xtick(x, pos):  # DO NOT REMOVE pos ARGUMENT (don't know why)
        if x % 10 == 0:
            return f'{int(x)}'
        else:
            return ''

    ax.xaxis.set_major_formatter(plt.FuncFormatter(custom_xtick))
    plt.tight_layout()
    ax.set_axisbelow(True)
    ax.set_title("")
    ax.grid(axis="x", linestyle="--", alpha=0.7, linewidth=0.5)

    plt.show()
