from collections import Counter
def find_uniq(arr):
    x = Counter(arr)
    for key in x:
        if x[key] == 1:
            return key
