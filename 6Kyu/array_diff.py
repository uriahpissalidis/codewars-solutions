def array_diff(a, b):
    if b == []:
        return a
    for num in b:
        while num in a:
            a.remove(num)
    return a
