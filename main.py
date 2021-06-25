import numpy as np


def minusSide(num):
    num -= 1

    return num


def plusSide(num):
    num += 1

    return num


if __name__ == '__main__':
    numB = 5
    midP = 2

    if numB == 5:
        z = np.zeros(shape=(numB, numB))
    elif (numB / 2) % 5 == 0:
        numB += 1
        z = np.zeros(shape=(numB, numB))

    z[0][midP] = 1

    numr = midP
    numl = midP

    for i in range(1, numB - 1):

        one = 0

        if i == 3:
            one = 1

        if one == 1:
            z[i][plusSide(numl)] = 1
            z[i][minusSide(numr)] = 1

        if one == 0:
            z[i][minusSide(numl)] = 1
            z[i][plusSide(numr)] = 1

            numl = minusSide(numl)
            numr = plusSide(numr)

    z[numB - 1][2] = 1

    print(z)
