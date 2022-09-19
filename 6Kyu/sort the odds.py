def sort_array(s):
    odds = []
    for num in s:
        if num%2:
            odds.append(num)
    odds.sort()
    for i in range(len(s)):
        if s[i]%2:
            s[i] = odds.pop(0)
    return s
