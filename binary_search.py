def binary_search(list, item):
    # Need our low and high nums to know where to start and end the next iteration
    low = 0
    high = len(list) - 1

    while low <= high: # while we haven't narrowed it down to 1 element
        print("Step") # printing the number of steps it takes to get the rigth answer
        mid = int((low + high) / 2) # finding the middle of the list, rounds down by default
        guess = list[mid] # we are guessing the middle of the array 
        #if the guess is too low, update `low` accordingly   
        if guess == item: # found the item!
            return mid
        if guess > item: # the guess was too high so
            high = mid - 1 # we set the middle as the new high, eliminating the last 50% of the list
        else:
            low = mid + 1 # the guess was too low, so we set the new low to mid + 1, eliminating the first 50% of the 
    return None

# any sorted array (must be sorted for binary search to work)
my_list = [1, 3, 5, 7, 9]
new_list = [x for x in range(0, 128)]

# print(binary_search(my_list, 3))
# print(binary_search(my_list, -1))
print(binary_search(new_list, 2))

