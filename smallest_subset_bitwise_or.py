
def smallest_subset(arr):
    max_or = 0
    for i in arr:
        max_or |= i

    tabl = [[] for _ in range(max_or+1)]

    for elem in arr:
        tabl[elem].append([elem])

    for i in range(1,max_or):
        for elem in arr:
            new_index = i | elem
            for entry in tabl[i]:
                if elem not in entry:
                    new_table_entry = entry + [elem]

                    tabl[new_index].append(new_table_entry)

    for i in range(max_or+1):
        print(tabl[i])

    smallest_size = len(arr)
    for entry in tabl[-1]:
        if len(entry) < smallest_size:
            smallest_size = len(entry)
    print(max_or)
    return smallest_size