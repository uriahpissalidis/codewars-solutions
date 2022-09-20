def duplicate_count(text):
    text = text.lower()
    if text == "": return 0
    seen, ans = {}, 0
    for char in text:
        if char not in seen:
            seen[char] = 1
        else:
            seen[char] += 1
    for key in seen:
        if seen[key] > 1: ans += 1
    return ans
