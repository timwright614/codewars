#jan/22 - https://www.codewars.com/kata/563b662a59afc2b5120000c6

def nb_year(p0, percent, aug, p):
    count = 0
    pop = p0
    newpop = p0
    while newpop<p:
        newpop = round((pop*(1+percent/100)+aug)-0.5)
        count += 1
        pop = newpop
    return count
