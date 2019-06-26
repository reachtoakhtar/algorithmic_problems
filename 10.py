def find_triplets(lst, sum):
    all_triplets = []
    l = len(lst)

    for i in range(l-1):
        s = dict()
        for j in range(i + 1, l):
            x = sum - (lst[i] + lst[j])
            if x in s.keys():
                all_triplets.append([x, lst[i], lst[j]])
            else:
                s[lst[j]] = 1

    return all_triplets

print(find_triplets([2, 9, 6, 8, 7], 17))
