import time
import numpy as np
from matplotlib import pyplot as plt
import math
import random

NUM = 5000
print("Pocet bodov je:", NUM * 4 + 20)
# NUM == [5 000] means 20000 + 20 points
# NUM == [2 500] means 10000 + 20 points
# NUM == [1 250] means 5000 + 20 points
# NUM == [625] means 2500 + 20 points


class ONE_DOT:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour
        self.distance = -1


def classify(x, y, k):  #funkcia na klasifikovanie farby danej bodky
    global number_of_training_data
    global endData

    for j in range(number_of_training_data):
        testData[j].distance = math.sqrt(((x-testData[j].x) ** 2) + ((y-testData[j].y) ** 2)) # vypocitavanie vzdialenosti bodov

    sortedTestData = sorted(testData, key=lambda z: z.distance) # zoradenie danych bodob podla vzdialenosti

    redNumber = 0
    greenNumber = 0
    blueNumber = 0
    purpleNumber = 0

    for j in range(k):
        if sortedTestData[j].colour == "red":
            redNumber += 1
        if sortedTestData[j].colour == "green":
            greenNumber += 1
        if sortedTestData[j].colour == "blue":
            blueNumber += 1
        if sortedTestData[j].colour == "purple":
            purpleNumber += 1

    finalColour = max(redNumber, greenNumber, blueNumber, purpleNumber)

    if finalColour == redNumber:
        endData.append(ONE_DOT(x, y, "red"))
        testData.append(ONE_DOT(x, y, "red"))
        return "red"

    if finalColour == greenNumber:
        endData.append(ONE_DOT(x, y, "green"))
        testData.append(ONE_DOT(x, y, "green"))
        return "green"

    if finalColour == blueNumber:
        endData.append(ONE_DOT(x, y, "blue"))
        testData.append(ONE_DOT(x, y, "blue"))
        return "blue"

    if finalColour == purpleNumber:
        endData.append(ONE_DOT(x, y, "purple"))
        testData.append(ONE_DOT(x, y, "purple"))
        return "purple"


R1 = ONE_DOT(-4500, -4400, "red")   # cvytváranie zaciatocnych bodov
R2 = ONE_DOT(-4100, -3000, "red")
R3 = ONE_DOT(-1800, -2400, "red")
R4 = ONE_DOT(-2500, -3400, "red")
R5 = ONE_DOT(-2000, -1400, "red")

G1 = ONE_DOT(+4500, -4400, "green")
G2 = ONE_DOT(+4100, -3000, "green")
G3 = ONE_DOT(+1800, -2400, "green")
G4 = ONE_DOT(+2500, -3400, "green")
G5 = ONE_DOT(+2000, -1400, "green")

B1 = ONE_DOT(-4500, +4400, "blue")
B2 = ONE_DOT(-4100, +3000, "blue")
B3 = ONE_DOT(-1800, +2400, "blue")
B4 = ONE_DOT(-2500, +3400, "blue")
B5 = ONE_DOT(-2000, +1400, "blue")

P1 = ONE_DOT(+4500, +4400, "purple")
P2 = ONE_DOT(+4100, +3000, "purple")
P3 = ONE_DOT(+1800, +2400, "purple")
P4 = ONE_DOT(+2500, +3400, "purple")
P5 = ONE_DOT(+2000, +1400, "purple")

endData = []
testData = []
testData.extend((R1, R2, R3, R4, R5, G1, G2, G3, G4, G5, B1, B2, B3, B4, B5, P1, P2, P3, P4, P5))
endData.extend((R1, R2, R3, R4, R5, G1, G2, G3, G4, G5, B1, B2, B3, B4, B5, P1, P2, P3, P4, P5))

red_good = []
green_good = []
blue_good = []
purple_good = []

for i in range(NUM):    # generovanie poctu bodov so spravnou suradnicou
    x_Coor = random.randint(-5000, 500)
    y_Coor = random.randint(-5000, 500)
    dot = ONE_DOT(x_Coor, y_Coor, "red")
    while dot in red_good:
        x_Coor = random.randint(-5000, 500)
        y_Coor = random.randint(-5000, 500)
        dot = ONE_DOT(x_Coor, y_Coor, "red")
    red_good.append(dot)

for i in range(NUM):
    x_Coor = random.randint(-500, 5000)
    y_Coor = random.randint(-5000, 500)
    dot = ONE_DOT(x_Coor, y_Coor, "green")
    while dot in red_good:
        x_Coor = random.randint(-500, 5000)
        y_Coor = random.randint(-5000, 500)
        dot = ONE_DOT(x_Coor, y_Coor, "green")
    green_good.append(dot)

for i in range(NUM):
    x_Coor = random.randint(-5000, 500)
    y_Coor = random.randint(-500, 5000)
    dot = ONE_DOT(x_Coor, y_Coor, "blue")
    while dot in red_good:
        x_Coor = random.randint(-5000, 500)
        y_Coor = random.randint(-500, 5000)
        dot = ONE_DOT(x_Coor, y_Coor, "Blue")
    blue_good.append(dot)

for i in range(NUM):
    x_Coor = random.randint(-500, 5000)
    y_Coor = random.randint(-500, 5000)
    dot = ONE_DOT(x_Coor, y_Coor, "purple")
    while dot in red_good:
        x_Coor = random.randint(-5000, 500)
        y_Coor = random.randint(-500, 5000)
        dot = ONE_DOT(x_Coor, y_Coor, "Purple")
    purple_good.append(dot)

red_wrong = []
green_wrong = []
blue_wrong = []
purple_wrong = []

for i in range(NUM):    # generovanie poctu bodov s nespravnou suradnicou
    while True:
        x_Coor = random.randint(-5000, 5000)
        y_Coor = random.randint(-5000, 5000)
        if x_Coor > 500 and y_Coor > 500:
            red_wrong.append(ONE_DOT(x_Coor, y_Coor, "red"))
            break

for i in range(NUM):
    while True:
        x_Coor = random.randint(-5000, 5000)
        y_Coor = random.randint(-5000, 5000)
        if x_Coor < -500 and y_Coor > 500:
            green_wrong.append(ONE_DOT(x_Coor, y_Coor, "green"))
            break

for i in range(NUM):
    while True:
        x_Coor = random.randint(-5000, 5000)
        y_Coor = random.randint(-5000, 5000)
        if x_Coor > 500 and y_Coor < -500:
            blue_wrong.append(ONE_DOT(x_Coor, y_Coor, "blue"))
            break

for i in range(NUM):
    while True:
        x_Coor = random.randint(-5000, 5000)
        y_Coor = random.randint(-5000, 5000)
        if x_Coor > 500 and y_Coor > 500:
            purple_wrong.append(ONE_DOT(x_Coor, y_Coor, "purple"))
            break

plt.xlim(-5000, 5000)   # vytvorenie platna
plt.ylim(-5000, 5000)
plt.yticks(np.arange(-5000, 6000, 1000))
plt.yticks(np.arange(-5000, 6000, 1000))
plt.xlabel("X")
plt.ylabel("Y")
fig, axs = plt.subplots(2, 2)
plt.suptitle('KNN algoritmus')

KNNList = [1, 3, 7, 15]
for i in range(4):

    r = 0
    g = 0
    b = 0
    p = 0

    red_count = 0
    blue_count = 0
    green_count = 0
    purple_count = 0

    colorList = ["red", "green", "blue", "purple"]
    previous = ""
    number_of_training_data = 20
    testData = []
    testData.extend((R1, R2, R3, R4, R5, G1, G2, G3, G4, G5, B1, B2, B3, B4, B5, P1, P2, P3, P4, P5))
    start = time.time()

    assigned = 0
    endData = []
    endData.extend((R1, R2, R3, R4, R5, G1, G2, G3, G4, G5, B1, B2, B3, B4, B5, P1, P2, P3, P4, P5))
    mistake = 0

    while True:
        if red_count == blue_count == green_count == purple_count == NUM:
            break

        x_Coor = 0
        y_Coor = 0

        while True:
            random_number = random.randint(0, 3)
            color = colorList[random_number]
            if red_count or blue_count or green_count or purple_count == 10000:
                break
            if color != previous:
                break

        if random.random() < 0.99:
            if color == "red":
                if red_count != NUM:
                    red_pop = red_good[r]
                    x_Coor = red_pop.x
                    y_Coor = red_pop.y
                    red_count += 1
                    r += 1
                    assigned = classify(x_Coor, y_Coor, KNNList[i])
                    number_of_training_data += 1

            if color == "green":
                if green_count != NUM:
                    green_pop = green_good[g]
                    x_Coor = green_pop.x
                    y_Coor = green_pop.y
                    green_count += 1
                    g += 1
                    assigned = classify(x_Coor, y_Coor, KNNList[i])
                    number_of_training_data += 1

            if color == "blue":
                if blue_count != NUM:
                    blue_pop = blue_good[b] 
                    x_Coor = blue_pop.x
                    y_Coor = blue_pop.y
                    blue_count += 1
                    b += 1
                    assigned = classify(x_Coor, y_Coor, KNNList[i])
                    number_of_training_data += 1

            if color == "purple":
                if purple_count != NUM:
                    purple_pop = purple_good[p]
                    x_Coor = purple_pop.x
                    y_Coor = purple_pop.y
                    purple_count += 1
                    p += 1
                    assigned = classify(x_Coor, y_Coor, KNNList[i])
                    number_of_training_data += 1

        else:
            if color == "red":
                if red_count != NUM:
                    red_pop = red_wrong[r]
                    x_Coor = red_pop.x
                    y_Coor = red_pop.y
                    red_count += 1
                    r += 1
                    assigned = classify(x_Coor, y_Coor, KNNList[i])
                    number_of_training_data += 1

            if color == "green":
                if green_count != NUM:
                    green_pop = green_wrong[g]
                    x_Coor = green_pop.x
                    y_Coor = green_pop.y
                    green_count += 1
                    g += 1
                    assigned = classify(x_Coor, y_Coor, KNNList[i])
                    number_of_training_data += 1

            if color == "blue":
                if blue_count != NUM:
                    blue_pop = blue_wrong[b]
                    x_Coor = blue_pop.x
                    y_Coor = blue_pop.y
                    blue_count += 1
                    b += 1
                    assigned = classify(x_Coor, y_Coor, KNNList[i])
                    number_of_training_data += 1

            if color == "purple":
                if purple_count != NUM:
                    purple_pop = purple_wrong[p]
                    x_Coor = purple_pop.x
                    y_Coor = purple_pop.y
                    purple_count += 1
                    p += 1
                    assigned = classify(x_Coor, y_Coor, KNNList[i])
                    number_of_training_data += 1
        
        if assigned != color:
            mistake += 1
        previous = assigned


    
    print("pocet chyb je: ", mistake)
    stop = time.time()
    print("cas trvavia generovania:", stop - start)


    for data in endData:
   
        if KNNList[i] == 15:
            axs[1, 1].plot(data.x, data.y, marker="o", color=data.colour)
            axs[1, 1].set_title(KNNList[i])

        if KNNList[i] == 7:
            axs[1, 0].plot(data.x, data.y, marker="o", color=data.colour)
            axs[1, 0].set_title(KNNList[i])

        if KNNList[i] == 3:
            axs[0, 1].plot(data.x, data.y, marker="o", color=data.colour)
            axs[0, 1].set_title(KNNList[i])

        if KNNList[i] == 1:
            axs[0, 0].plot(data.x, data.y, marker="o", color=data.colour)
            axs[0, 0].set_title(KNNList[i])

        

fig.tight_layout()
plt.savefig("KNN_DALSI")
print("koniec programu")