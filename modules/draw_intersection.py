import matplotlib.pyplot as plt
import numpy as np


def draw_inter_method_choice(values, inpt):

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
    fig, ax = plt.subplots(figsize=(10, 5), dpi=600)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    return fig, ax

"""[0] - main cycle duration, [1] - secondary cycle duration, [2] - main green cycle, [3] - secondary green cycle,
        [4] - main intergreen time, [5] - secondary intergreen time, [6] - yellow time, [7] - red-yellow time [8] - k_main_duration,
        [9] - k_secondary_duration, [10] - main short red, [11] - secondary short red, [12] - main long red, [13] - secondary long red,
        [14] - full cycle duration"""


def draw_k_one(ax, values, barheight, colors):
    """Draw green"""
    ax.barh(3, values[2], left= 0, height = barheight, color=colors[1], edgecolor='black')
    ax.text(values[2] / 2, 3 + barheight / 2, f'{values[2]}s', ha='center', va='bottom', color='black')

    """Draw yellow"""
    ax.barh(3, values[6], left=values[2], height=barheight, color=colors[2], edgecolor='black')
    ax.text(values[2]+values[6] / 2, 3 + barheight / 2, f'{values[6]}s', ha='center', va='bottom', color='black')
    ax.plot([values[2], values[2]+ values[6]], [3-barheight*0.5, 3+barheight*0.5], color='black')

    """Draw short red"""
    ax.barh(3, values[10], left=values[2]+values[6], height=barheight, color=colors[0], edgecolor='black')
    ax.text(values[2] + values[6] + values[10]/2, 3+barheight/2, f'{values[10]}s', ha='center', va='bottom', color='black')
    ax.plot([values[2]+values[6], values[2]+values[6]+values[10]], [3, 3], color='black')

    """Draw red yellow"""
    ax.add_patch(plt.Rectangle((values[14] - values[7], 3),values[7],barheight * 0.5, facecolor=colors[0], edgecolor='black'))
    ax.add_patch(
        plt.Rectangle((values[14] - values[7], 3-barheight*0.5), values[7], barheight * 0.5, facecolor=colors[2], edgecolor='black'))
    ax.plot([values[14]-values[7], values[14]], [3-barheight*0.5, 3+barheight*0.5], color='black')
    ax.text(values[14]-values[7]/2, 3+barheight*0.5, f'{values[7]}s', ha='center', va='bottom', color='black')

    """Draw red"""
    ax.barh(3, values[14]-(values[2]+values[6]+values[10]+values[7]), left=values[2]+values[6]+values[10], height=barheight,
            color=colors[0], edgecolor='black')
    ax.text(values[2]+values[6]+values[10]+(values[14]-(values[2]+values[6]+values[10]+values[7]))/2, 3+barheight*0.5,
            f'{values[14] - (values[2] + values[6] + values[10] + values[7]):.0f}s', ha='center', va='bottom', color='black')
    ax.plot([values[2]+values[6]+values[10], values[2]+values[6]+values[10] + (values[14] - (values[2] + values[6] + values[10] + values[7]))],
            [3,3], color='black')

def draw_k_two(ax, values, barheight, colors):
    """Draw red"""
    ax.barh(2, values[2]+values[6]+values[10]-values[7], left=0, height=barheight, color=colors[0], edgecolor='black')
    ax.text((values[2]+values[6]+values[10]-values[7])/2, 2+barheight*0.5, f'{(values[2]+values[6]+values[10]-values[7]):.0f}s',
            ha='center', va='bottom', color='black')
    ax.plot([0, values[2]+values[6]+values[10]-values[7]], [2, 2], color='black')

    """Draw red-yellow"""
    ax.add_patch(
        plt.Rectangle((values[2]+values[6]+values[10]-values[7], 2), values[7], barheight * 0.5, facecolor=colors[0], edgecolor='black'))
    ax.add_patch(
        plt.Rectangle((values[2] + values[6] + values[10] - values[7], 2-barheight*0.5), values[7], barheight * 0.5, facecolor=colors[2],
                      edgecolor='black'))
    ax.text(values[2]+values[6]+values[10]-(values[7]*0.5), 2 + barheight * 0.5,
            f'{values[7]:.0f}s',
            ha='center', va='bottom', color='black')
    ax.plot([values[2]+values[6]+values[10]-values[7], values[2]+values[6]+values[10]], [2-barheight*0.5, 2+barheight*0.5], color='black')

    """Draw green"""
    ax.barh(2, values[2], left=values[2]+values[6]+values[10], height=barheight, color=colors[1], edgecolor='black')
    ax.text(values[2]+values[6]+values[10]+(values[2] * 0.5), 2 + barheight * 0.5,
            f'{values[2]:.0f}s',
            ha='center', va='bottom', color='black')

    """Draw yellow"""
    ax.barh(2, values[6], left=values[2]+values[6]+values[10]+values[2], height=barheight, color=colors[2], edgecolor='black')
    ax.text(values[2]+values[6]+values[10]+values[2]+(values[6] * 0.5), 2 + barheight * 0.5,
            f'{values[6]:.0f}s',
            ha='center', va='bottom', color='black')
    ax.plot([values[2]+values[6]+values[10]+values[2], values[2]+values[6]+values[10]+values[2] + values[6]],
            [2 - barheight * 0.5, 2 + barheight * 0.5], color='black')

    """Draw intergreen"""
    ax.barh(2, values[10], left=values[2]+values[6]+values[10]+values[2]+values[6], height=barheight, color=colors[0], edgecolor='black')
    ax.text(values[2]+values[6]+values[10]+values[2]+values[6]+(values[10] * 0.5), 2 + barheight * 0.5,
            f'{values[10]:.0f}s',
            ha='center', va='bottom', color='black')
    ax.plot([values[2]+values[6]+values[10]+values[2]+values[6], values[2]+values[6]+values[10]+values[2]+values[6]+values[10]], [2, 2], color='black')

    """Draw red"""
    ax.barh(2, values[14]-(values[2]+values[6]+values[10]+values[2]+values[6]+values[10]), left=values[2]+values[6]+values[10]+values[2]+values[6]+values[10],
            height=barheight, color=colors[0], edgecolor='black')
    ax.text(values[2]+values[6]+values[10]+values[2]+values[6]+values[10]+((values[14]-(values[2]+values[6]+values[10]+values[2]+values[6]+values[10]))* 0.5), 2 + barheight * 0.5,
            f'{values[14]-(values[2]+values[6]+values[10]+values[2]+values[6]+values[10]):.0f}s',
            ha='center', va='bottom', color='black')
    ax.plot([values[2]+values[6]+values[10]+values[2]+values[6]+values[10],
             values[2]+values[6]+values[10]+values[2]+values[6]+values[10]+values[14]-(values[2]+values[6]+values[10]+values[2]+values[6]+values[10])], [2, 2], color='black')

def draw_k_three(ax, values, barheight,colors):
    """Draw red"""
    ax.barh(1,(values[2]+values[6]+values[10]+values[2]+values[6]+values[10]-values[7]), left=0, height=barheight,
            color=colors[0], edgecolor='black')
    ax.text(((values[2]+values[6]+values[10]+values[2]+values[6]+values[10]-values[7]) * 0.5),
            1 + barheight * 0.5,
            f'{(values[2]+values[6]+values[10]+values[2]+values[6]+values[10]-values[7]):.0f}s',
            ha='center', va='bottom', color='black')
    ax.plot([0, (values[2]+values[6]+values[10]+values[2]+values[6]+values[10]-values[7])], [1,1], color='black')

    """Draw red-yelow"""
    ax.add_patch(
        plt.Rectangle((values[2]+values[6]+values[10]+values[2]+values[6]+values[10]-values[7], 1), values[7], barheight * 0.5,
                      facecolor=colors[0], edgecolor='black'))
    ax.add_patch(
        plt.Rectangle((values[2] + values[6] + values[10] + values[2] + values[6] + values[10] - values[7], 1-barheight*0.5),
                      values[7], barheight * 0.5,
                      facecolor=colors[2], edgecolor='black'))
    ax.text((values[2] + values[6] + values[10] + values[2] + values[6] + values[10] - (values[7]) * 0.5),
            1 + barheight * 0.5,
            f'{values[7]:.0f}s',
            ha='center', va='bottom', color='black')
    ax.plot([values[2]+values[6]+values[10]+values[2]+values[6]+values[10]-values[7],
             values[2]+values[6]+values[10]+values[2]+values[6]+values[10]], [1-barheight*0.5, 1+barheight*0.5],
            color='black')

    """Draw green"""
    ax.barh(1, values[3], left=(values[2] + values[6] + values[10] + values[2] + values[6] + values[10]), height=barheight,
            color=colors[1], edgecolor='black')
    ax.text((values[2] + values[6] + values[10] + values[2] + values[6] + values[10] + (values[3] * 0.5)),
            1 + barheight * 0.5,
            f'{values[3]:.0f}s',
            ha='center', va='bottom', color='black')

    """Draw yellow"""
    ax.barh(1, values[6], left=(values[2] + values[6] + values[10] + values[2] + values[6] + values[10]+values[3]), height=barheight, color=colors[2], edgecolor='black')
    ax.text((values[2] + values[6] + values[10] + values[2] + values[6] + values[10]+values[3]+ (values[6] * 0.5)),
            1 + barheight * 0.5,
            f'{values[6]:.0f}s',
            ha='center', va='bottom', color='black')
    ax.plot([values[2] + values[6] + values[10] + values[2] + values[6] + values[10]+values[3],
             values[2] + values[6] + values[10] + values[2] + values[6] + values[10]+values[3]+values[6]], [1-barheight*0.5, 1+barheight*0.5],
            color='black')

    """Draw intergreen"""
    ax.barh(1, values[11], left = values[14]-values[11], height=barheight, color=colors[0], edgecolor='black')
    ax.text((values[14]-values[11] + (values[11] * 0.5)),
            1 + barheight * 0.5,
            f'{values[11]:.0f}s',
            ha='center', va='bottom', color='black')
    ax.plot([values[14]-values[11], values[14]], [1,1], color='black')
def format_axes(ax, values):
    """Configure y-ticks, x-ticks, grid, and labels."""
    ax.set_yticks([1, 2, 3])
    ax.set_yticklabels(["K 3","K 2", "K 1"])
    ax.tick_params(axis="y", length=0)

    ax.set_xticks(np.arange(0, values[14] + 1, 1))
    ax.set_xlim(0, values[14] + 0.1)
    ax.set_xlabel("")
    ax.tick_params(axis="x", labelsize=8)

    def custom_xtick(x, pos):  # DO NOT REMOVE pos ARGUMENT (don't know why, but it's crucial)
        if x % 10 == 0 or x == values[14]:
            return f'{int(x)}'
        else:
            return ''

    ax.xaxis.set_major_formatter(plt.FuncFormatter(custom_xtick))
    plt.tight_layout()
    ax.set_axisbelow(True)
    ax.set_title("")
    ax.grid(axis="x", linestyle="-", alpha=0.7, linewidth=0.5)

def draw_legend(colors):
    pass

def draw(values, colors):
    """Main drawing function that ties everything together."""
    fig, ax = setup_figure_and_axes()

    # barheight calculation
    barheight = 15 * 0.0393700787  # 2 mm to inches

    # draw all bars
    draw_k_one(ax, values, barheight, colors)
    draw_k_two(ax, values, barheight, colors)
    draw_k_three(ax, values, barheight, colors)

    # format the axes, ticks, grid, etc.
    format_axes(ax, values)

    # finally, show the plot
    plt.show()
