#06/07/22 - https://www.codewars.com/kata/52b7ed099cdc285c300001cd

def sum_of_intervals(intervals):
    max_upper = max([i[1] for i in intervals])

    interval_index = [i[0]+i[1]/max_upper for i in intervals]

    intervals_sorted = [i for i,index in sorted(zip(intervals,interval_index))]

    intervals_no_overlap = []

    for i in intervals_sorted:
        if len(intervals_no_overlap) == 0:
            intervals_no_overlap.append(i)
        elif i[0] >= intervals_no_overlap[-1][1]:
            intervals_no_overlap.append(i)
        elif i[1] > intervals_no_overlap[-1][1]:
            intervals_no_overlap.append([intervals_no_overlap[-1][1],i[1]])

    no_overlap_span = 0

    for i in intervals_no_overlap:
        no_overlap_span += i[1]-i[0]

    return no_overlap_span
