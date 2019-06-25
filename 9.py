s = "abc"

def permute(s, i, length, lst):
    if i == length:
        lst.append(''.join(s))
    else:
        for j in range(i,length):
            # Swap
            s[i], s[j] = s[j], s[i]
            permute(s, i+1, length, lst)
            s[i], s[j] = s[j], s[i]

    return lst

print(permute(list(s), 0, len(s), []))
