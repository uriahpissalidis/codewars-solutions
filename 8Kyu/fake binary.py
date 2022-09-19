def fake_bin(x):
    xx = ''
    for i in range(0, len(x)):
        if x[i] >= '5':
            xx += '1'
        else:
            xx += '0'
    return xx
