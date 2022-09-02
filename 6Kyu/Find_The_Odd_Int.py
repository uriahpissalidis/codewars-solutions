from collections import defaultdict
def find_it(seq):
    if len(seq) == 1: return seq[0]
    d = defaultdict(int)
    for num in seq:
        d[num] += 1
    for key in d:
        if d[key]%2==1:
            return key
