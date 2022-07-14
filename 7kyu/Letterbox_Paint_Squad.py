#14/01/22 - https://www.codewars.com/kata/597d75744f4190857a00008d

def paint_letterboxes(start, finish):

    digits=[]
    for i in range(start,finish+1):
        digits.extend(list(str(i)))

    counts=[]
    for i in range(10):
        count=0
        for j in digits:
            if i==int(j):
                count+=1
        counts.append(count)
    return counts
