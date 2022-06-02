#! /usr/bin/env nix-shell
#! nix-shell default.nix -i python


import matplotlib.pyplot as plt
import random


class Shrimp():
    def __init__(self, pos, mapSize):
        # The position of the shrimp as x & y values stored in a list
        self.pos = pos
        self.mapSize = mapSize

    def stepChange(self):
        self.pos[0] += random.randint(-10, 10)
        self.pos[1] += random.randint(-10, 10)

        # If the shrimp moved off the map, move it back on
        if self.pos[0] < 0:
            self.pos[0] = 0
        elif self.pos[0] >= self.mapSize[0]:
            self.pos[0] = self.mapSize[0]

        if self.pos[1] < 0:
            self.pos[1] = 0
        elif self.pos[1] >= self.mapSize[1]:
            self.pos[1] = self.mapSize[1]



XMAX = 1000
YMAX = 500

def main():
    shrimpList = []
    numOfShrimp = int(15)

    showing_text = input("Would you like to show the plot ? [Y/N] :").lower()

    if showing_text == "n":
        showing = False
    else:
        showing = True

    for i in range(numOfShrimp):
        randX = random.randint(0, XMAX)
        randY = random.randint(0, YMAX)
        shrimpList.append(Shrimp([randX, randY], [XMAX, YMAX]))

    total_of_shrimps = int()

    for b in range(15):
        xvalues = []
        yvalues = []
        for shrimp in shrimpList:
            shrimp.stepChange()
            xvalues.append(shrimp.pos[0])
            yvalues.append(shrimp.pos[1])

        total_of_shrimps = int(numOfShrimp * 0.08)
        # Shrimp multiply at a rate of 8%
        for c in range(total_of_shrimps):
            randX = random.randint(0, XMAX)
            randY = random.randint(0, YMAX)
            shrimpList.append(Shrimp([randX, randY], [XMAX, YMAX]))

        if showing:
            plt.scatter(xvalues, yvalues)   # Note plt origin is bottom left
            plt.xlim(0,XMAX)
            plt.ylim(0,YMAX)
            plt.pause(0.1)
            plt.clf()


    if not showing:
        print(f"({numOfShrimp}, {len(shrimpList)})")


if __name__ == "__main__":
    main()