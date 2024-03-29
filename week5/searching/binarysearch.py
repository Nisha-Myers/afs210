def binary_search(list, term):
    start = 0 # First index
    last = len(list) - 1 # Last index

    while start <= last: # While the number isn't found

        middle = start + (last - start) // 2 # Calculate middle point in the list

        if list[middle] == term: # If middle of list is equal to term
            return True 
        elif list[middle] < term: # If the middle of the list is less than term, search left side, else, search right side.
            start = middle + 1
        else:
            last = middle - 1
    return False


        

my_list = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
print(binary_search(my_list, 31)) # Find 31
print(binary_search(my_list, 77)) # Find 77

my_list_2 = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]
print(binary_search(my_list_2, "Delta")) # Find "Delta"