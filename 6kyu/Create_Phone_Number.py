#jan/22 - https://www.codewars.com/kata/525f50e3b73515a6db000b83

def create_phone_number(n):

    n_joined = ''.join(str(i) for i in n)

    return f'({n_joined[0:3]}) {n_joined[3:6]}-{n_joined[6:]}'
