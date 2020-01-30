def quicksort(list):
    print("quicksort!")
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i <= pivot]

        greater = [i for i in list [1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))
print(quicksort([2, 50, 19, 39, 1, 0, 15, 18, 60]))