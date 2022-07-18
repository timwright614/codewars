#14/01/22 - https://www.codewars.com/kata/5acbc3b3481ebb23a400007d

def is_flush(cards):
    cardsuits=[]
    for i in cards:
        suit=list(i)[-1]
        cardsuits.append(suit)
    if len(set(cardsuits))==1:
        return True
    else:
        return False
