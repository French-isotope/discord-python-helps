import matplotlib.animation as animation
import matplotlib.pyplot as plt
import random
import sys

sys.path.insert(0, 'algorithms/')
from algorithms import bubblesort


def visualize(nums=30):
    colours = ["#202729", "#fafafa", "#d32ce6"]
    data = list(range(1, nums + 1))
    random.shuffle(data)
    generator = bubblesort.bubblesort(data)

    fig, ax = plt.subplots(facecolor=colours[0])
    ax.set_facecolor(colours[0])
    plt.xticks([])
    plt.yticks([])

    ax.set_xlim(0, nums)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes, color=colours[1])
    ax.set_title("Bubble Sort", color=colours[1])

    bar_sub = ax.bar(range(len(data)), data, align="edge", color=colours[2])
    iteration = [0]

    def update(data, rects, iteration):
        for rect, val in zip(rects, data):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}")

    anim = animation.FuncAnimation(
        fig,
        func=update,
        fargs=(bar_sub, iteration),
        frames=generator,
        repeat=True,
        blit=False,
        interval=15,
        save_count=90000,
    )

    # for showing the animation on screen
    plt.show()
    plt.close()


if __name__ == "__main__":
    visualize()

Envoyer
un
message
à @ Earwarmers
