from random import randint


def generate_random_list(n):
    return [randint(0, 100) for i in range(n)]
NUMBERS_TO_SORT = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]  # some random numbers

# sort the list in ascending order
def sort_list_1():
    l = NUMBERS_TO_SORT.copy()  # Create a copy of list to sort
    n = len(l)
    for i in range(n):
        for j in range(0, n - i - 1):
            if l[j] > l[j + 1]: # check if the number is bigger than the next element
                # if so, swap the elements
                l[j], l[j + 1] = l[j + 1], l[j]
                # continue until the list is sorted
    return l'

def sort_list_2():
    l = NUMBERS_TO_SORT.copy()  # Create a copy of list to sort
    n = len(l) # get the length of the list
   # is_sorted = False # set the flag to False
    swap_count = None

    while not (swap_count == 0):
        swap_count = 0
        for i in range(0, n - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                print(l)
                swap_count += 1

    return l

if __name__ == "__main__":
    #NUMBERS_TO_SORT = generate_random_list(100)
    NUMBERS_TO_SORT = input("Enter a list of numbers separated by spaces: ").split(" ")
    print(f"Unsorted: {NUMBERS_TO_SORT}")

    sorted_list = sort_list_2()
    print(f"Sorted: {sorted_list}")
