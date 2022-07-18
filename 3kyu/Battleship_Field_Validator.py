#feb/22 - https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7

import numpy

fleet = [[1,1,1,1],[1,1,1],[1,1,1],[1,1],[1,1],[1,1],[1],[1],[1],[1]]

testfleet = [[1,1,1,1,1]]
for x in fleet:
    testfleet.append(x)
    testfleet.append(x)

remainder = [[1,1,1,1,1]]
for x in fleet:
    remainder.append(x)

def finder(ship,field):
    ship_len = len(ship)
    for i in field:
        for j in range(len(i)-ship_len+1):
            if i[j:(j+ship_len)] == ship:
                i[j:(j+ship_len)] = [0 for x in range(ship_len)]

                return True
    return False

def transpose(x):
    return (numpy.array(x).T.tolist())


def touching(x):

    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == 1:
                _12and6 = []
                diags = []
                _3and9 = []

                if i > 0:
                    _12and6.append(x[i-1][j])
                    if j > 0:
                        diags.append(x[i-1][j-1])
                    if j < 9:
                        diags.append(x[i-1][j+1])

                if j > 0:
                    _3and9.append(x[i][j-1])

                if j < 9:
                    _3and9.append(x[i][j+1])

                if i < 9:
                    _12and6.append(x[i+1][j])
                    if j > 0:
                        diags.append(x[i+1][j-1])
                    if j < 9:
                        diags.append(x[i+1][j+1])


                if sum(_12and6) > 1 and sum(_3and9) > 1:
                    return True

                if 1 in diags:
                    return True

def validate_battlefield(field):

    x = field

    if touching(x):

        return False


    field_W = x.copy()
    fleet_W = testfleet.copy()

    for i in testfleet:

        stop = False
        if finder(i,field_W):
            fleet_W.remove(i)
            stop = True

        if stop == False:

            field_W_trans = transpose(field_W)

            if finder(i,field_W_trans):
                fleet_W.remove(i)

            field_W = transpose(field_W_trans)

    water_empty = True
    for i in field_W:
        if 1 in i:
            water_empty = False
            break

    if fleet_W == remainder and water_empty:

        return True

    else:
        return False
