from collections import Counter
def xo(s):
    s = s.lower()
    c = Counter(s)
    return c['x'] == c['o']
