import math
def find_short(s):
    x = s.split(" ")
    d = {}
    ans = math.inf
    for word in x:
        d[word] = len(word)
    for word in d:
        ans = min(d[word], ans)
    return ans
