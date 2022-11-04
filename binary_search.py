def binar_serch(list, nums):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = low + high
        guess = list[mid]

        if guess == nums:
            return mid
        if guess > nums:
            high = mid - 1
        else:
            low = mid + 1
    return None


list_1 = [1, 2, 3, 4, 5, 6, 7]

print(binar_serch(list_1, 4))

# http://aliev.me/runestone/SortSearch/TheBinarySearch.html
