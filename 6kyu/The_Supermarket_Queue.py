# jan/22 - https://www.codewars.com/kata/57b06f90e298a7b53d000a86

def queue_time(customers, n):

    tills = []
    for i in range(n):
        tills.append([])

    for i in customers:
        tills[0].append(i)
        tills.sort(key = lambda x: sum(x))

    return sum(tills[-1])
