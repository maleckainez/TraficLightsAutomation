import matplotlib.pyplot as plt
import numpy as np


def draw_method_choice(values):
    inpt = int(input("enter 1 for color, 2 for black and white: \n"))
    colors = ['red', 'green', 'yellow']
    colors_bw = ['white', 'white', 'white']
    if inpt == 1:
        draw(values, colors)
    elif inpt == 2:
        draw(values, colors_bw)
    else:
        print("wrong input")


# [length_of_cycle (0), duration_green (1), intergreen_cycle (2),
#  yellow_red_duration (3), yellow_duration (4), k_duration (5),
#  k_short_red (6), k_long_red (7)]

def setup_figure_and_axes():
    """Create figure and axes with hidden spines."""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    return fig, ax


def draw_bars(ax, values, barheight, colors):
    """Draw all bars (green, yellow, intergreen red, long red, red-yellow)."""
    for i, start_time in zip([1, 0], [0, values[5]]):  # K1 and K2
        y_axis = i
        # draw green light
        ax.barh(y_axis, values[1], left=start_time, height=barheight,
                color=colors[1], edgecolor='black')
        ax.text(start_time + values[1] / 2, y_axis + barheight / 2,
                f'{values[1]}s', ha='center', va='bottom', color='black')

        # draw yellow light
        ax.barh(y_axis, values[4], left=start_time + values[1], height=barheight,
                color=colors[2], edgecolor='black')
        ax.plot([start_time + values[1], start_time + values[1] + values[4]], [y_axis - barheight * 0.5, y_axis + barheight * 0.5], color= 'black')
        ax.text(start_time + values[1] + values[4] / 2, y_axis + barheight / 2,
                f'{values[4]}s', ha='center', va='bottom', color='black')

        # draw intergreen red
        ax.barh(y_axis, values[6], left=start_time + values[1] + values[4],
                height=barheight, color=colors[0], edgecolor='black')
        ax.text(start_time + values[1] + values[4] + values[6] / 2,
                y_axis + barheight / 2, f'{values[6]}s',
                ha='center', va='bottom', color='black')
        ax.plot([start_time + values[1] + values[4], start_time + values[1] + values[4] + values[6]],
                [y_axis, y_axis], color='black')


        # draw long red and red-yellow
        if start_time == 0:
            # long-red
            ax.barh(y_axis, values[7], height=barheight,
                    left=start_time + values[5], color=colors[0], edgecolor='black')
            ax.text(start_time + values[5] + values[7] / 2,
                    y_axis + barheight / 2, f'{values[7]}s',
                    ha='center', va='bottom', color='black')
            ax.plot([start_time + values[5], start_time + values[5] + values[7]],
                    [y_axis, y_axis], color='black')

            # red part of red-yellow
            ax.add_patch(plt.Rectangle(
                (start_time + values[5] + values[7], y_axis),
                values[3],
                barheight * 0.5,
                facecolor=colors[0],
                edgecolor='black'
            ))

            # yellow part of red-yellow
            ax.add_patch(plt.Rectangle(
                (start_time + values[5] + values[7], y_axis - barheight * 0.5),
                values[3],
                barheight * 0.5,
                facecolor=colors[2],
                edgecolor='black'
            ))
            ax.plot([start_time + values[5] + values[7], start_time + values[5] + values[7] + values[3]],
                    [y_axis - barheight * 0.5, y_axis + barheight * 0.5], color='black')
            ax.text(start_time + values[5] + values[7] + values[3] / 2,
                    y_axis + barheight / 2, f'{values[3]}s',
                    ha='center', va='bottom', color='black')

        elif start_time == values[5]:
            ax.barh(y_axis, values[7], height=barheight,
                    left=start_time - values[5], color=colors[0], edgecolor='black')
            ax.text(start_time - values[5] + values[7] / 2,
                    y_axis + barheight / 2, f'{values[7]}s',
                    ha='center', va='bottom', color='black')
            ax.plot([start_time - values[5], start_time - values[5] + values[7]],
                    [y_axis, y_axis], color='black')

            ax.add_patch(plt.Rectangle(
                (start_time - values[3], y_axis),
                values[3],
                barheight * 0.5,
                facecolor=colors[0],
                edgecolor='black'
            ))
            # yellow part of red-yellow
            ax.add_patch(plt.Rectangle(
                (start_time - values[3], y_axis - barheight * 0.5),
                values[3],
                barheight * 0.5,
                facecolor=colors[2],
                edgecolor='black'
            ))
            ax.plot([start_time - values[3], start_time],
                    [y_axis - barheight * 0.5, y_axis + barheight * 0.5], color='black')
            ax.text(start_time - values[3] + values[3] / 2,
                    y_axis + barheight / 2, f'{values[3]}s',
                    ha='center', va='bottom', color='black')


def format_axes(ax, values):
    """Configure y-ticks, x-ticks, grid, and labels."""
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["K 2", "K 1"])
    ax.tick_params(axis="y", length=0)

    ax.set_xticks(np.arange(0, values[0] + 1, 1))
    ax.set_xlim(0, values[0] + 1)
    ax.set_xlabel("")
    ax.tick_params(axis="x", labelsize=8)

    def custom_xtick(x, pos):  # DO NOT REMOVE pos ARGUMENT
        if x % 10 == 0 or x == values[0]:
            return f'{int(x)}'
        else:
            return ''

    ax.xaxis.set_major_formatter(plt.FuncFormatter(custom_xtick))
    plt.tight_layout()
    ax.set_axisbelow(True)
    ax.set_title("")
    ax.grid(axis="x", linestyle="--", alpha=0.7, linewidth=0.5)


def draw(values, colors):
    """Main drawing function that ties everything together."""
    fig, ax = setup_figure_and_axes()

    # barheight calculation
    barheight = 15 * 0.0393700787  # 2 mm to inches

    # draw all bars
    draw_bars(ax, values, barheight, colors)

    # format the axes, ticks, grid, etc.
    format_axes(ax, values)

    # finally, show the plot
    plt.show()
