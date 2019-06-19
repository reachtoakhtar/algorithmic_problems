def count_currency(amount):
    notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    note_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    counter_dict = dict()
    for i, j in zip(notes, note_counter):
        if amount >= i:
            j = amount // i
            amount = amount - j * i
            counter_dict[i] = j

    return counter_dict


print("{currency: count}")
print(count_currency(2002))
