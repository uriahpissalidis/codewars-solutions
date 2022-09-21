def delete_nth(order,max_e):
    popOrder = order[::-1]
    d = {}
    for num in order:
        if num not in d:
            d[num] = 1
        else:
            d[num] += 1
        while d[num] > max_e:
            d[num] -= 1
            popOrder.pop(popOrder.index(num))
    return popOrder[::-1]
