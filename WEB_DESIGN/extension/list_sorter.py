NUMBERS_TO_SORT = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]  # some random numbers

print(f"Unsorted: {NUMBERS_TO_SORT}")

# sort the list in ascending order 
def sort_list():
    """Sort the list"""
    sorted_list = NUMBERS_TO_SORT.copy()  # Create a copy of list to sort
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                # swap the elements
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    print(f"Sorted: {sorted_list}")

if __name__ == "__main__":
    sort_list()
