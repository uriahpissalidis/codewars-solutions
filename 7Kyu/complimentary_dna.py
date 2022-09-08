def DNA_strand(dna):
    s, count = list(dna), 0
    for char in s:
        if char == 'A':
            s[count] = 'T'
            count+=1
        if char == 'T':
            s[count] = 'A'
            count+=1
        if char == 'C':
            s[count] = 'G'
            count+=1
        if char == 'G':
            s[count] = 'C'
            count+=1
    return "".join(s)
