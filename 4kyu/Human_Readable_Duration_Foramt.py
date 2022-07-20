# 11/07/22 - https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(seconds):

    if seconds == 0:
        return 'now'

    M = 60
    H = M*60
    D = H*24
    Y = D*365

    y = seconds // Y
    d = (seconds - y*Y) // D
    h = (seconds - y*Y - d*D) // H
    m = (seconds - y*Y - d*D - h*H) // M
    s = seconds - y*Y - d*D - h*H - m*M

    time = [y,d,h,m,s]

    units = ['year', 'day', 'hour', 'minute', 'second']

    time_as_strings = []

    for i in range(5):
        if 1 >= time[i] > 0:
            time_as_strings.append(str(time[i]) + ' ' + units[i])
        elif time[i] > 1:
            time_as_strings.append(str(time[i]) + ' ' + units[i]+'s')

    seperators = ['',' and ',', ',', ',', ']

    human_readable = ''

    for i in range(len(time_as_strings)):
        human_readable = time_as_strings[-(i+1)] + seperators[i] + human_readable

    return human_readable
