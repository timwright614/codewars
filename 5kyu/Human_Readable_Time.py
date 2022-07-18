# jan/22 .pyhttps://www.codewars.com/kata/52685f7382004e774f0001f7

def make_readable(seconds):

    import math

    part1 = math.floor(seconds/3600)
    part1_rem = seconds%3600
    part2 = math.floor(part1_rem/60)
    part2_rem = part1_rem%60
    part3 = part2_rem

    p1_string = str(part1)
    if len(p1_string) == 1:
        p1_string='0' + p1_string

    p2_string = str(part2)
    if len(p2_string) == 1:
        p2_string='0' + p2_string

    p3_string = str(part3)
    if len(p3_string) == 1:
        p3_string='0' + p3_string

    time=p1_string+':'+p2_string+':'+p3_string

    return time
