import re

def solution(files):
    lst = [re.split('([0-9]+)',f) for f in files]
    lst = sorted(lst, key = lambda x : (x[0].upper(),int(x[1]) ))

    return [''.join(file) for file in lst]
