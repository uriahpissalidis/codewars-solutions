def count_positives_sum_negatives(arr):
    if len(arr)==0: return []
    x, y = 0, 0
    for num in arr:
        if num > 0:
            x += 1
        else:
            y += num
    return [x,y]
