# jan/22 - https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def snail(snail_map):

    import copy
    inp_arr = copy.deepcopy(snail_map)
    out = []

    while inp_arr != []:

        out.extend(inp_arr.pop(0))
        if inp_arr == []:
            break

        rightside=[]
        for i in range(len(inp_arr)):
            rightside.append(inp_arr[i].pop(-1))

        out.extend(rightside)

        if inp_arr == []:
            break

        revrow=(inp_arr.pop(-1))
        revrow.reverse()
        out.extend(revrow)

        if inp_arr == []:
            break

        leftside = []
        for i in range(len(inp_arr)-1,-1,-1):
            leftside.append(inp_arr[i].pop(0))

        out.extend(leftside)

    return out
