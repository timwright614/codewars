#11/07/22 https://www.codewars.com/kata/58c5577d61aefcf3ff000081

def encode_rail_fence_cipher(string, n):

    decoded = string

    up = list(range(0,n-1))
    back = list(range(n-1,0,-1))
    up_back = up+back
    sequence = ((len(decoded)//n+1)*up_back)[:len(decoded)]

    encoded_rails = [[] for i in range(n)]

    for i in range(len(decoded)):
        encoded_rails[sequence[i]].append(decoded[i])

    encoded = ''
    for i in encoded_rails:
        encoded += ''.join(i)

    return encoded

def decode_rail_fence_cipher(string, n):

    encoded = string

    up = list(range(0,n-1))
    back = list(range(n-1,0,-1))
    up_back = up+back
    sequence = ((len(encoded)//n+1)*up_back)[:len(encoded)]

    decode_rails = [[] for i in range(n)]

    for i in range(len(encoded)):
        decode_rails[sequence[i]].append(i)

    decode_sequence = []
    for i in decode_rails:
        decode_sequence.extend(i)

    decoded_list = list(encoded)

    for i,j in zip(encoded,decode_sequence):
        decoded_list[j] = i

    decoded = ''.join(decoded_list)

    return decoded
