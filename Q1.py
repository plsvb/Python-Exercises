import random
import timeit
import numpy as np

def sorted_list_native(lst):
    if not lst:
        raise ValueError("Input list is empty.")
    if any(not isinstance(x, (int, float)) for x in lst):
        raise ValueError("List contains non-numerical values.")
    return sorted(lst)

def sorted_list_numpy(lst):
    if not lst:
        raise ValueError("Input list is empty.")
    if any(not isinstance(x, (int, float)) for x in lst):
        raise ValueError("List contains non-numerical values.")
    return np.sort(lst).tolist()

def time_and_sort(lst, function, description, file):
    try:
        start_time = timeit.default_timer()
        sorted_lst = function(lst)
        elapsed = timeit.default_timer() - start_time
        file.write(f"Time taken by {description}: {elapsed:.6f} seconds\n")
        return sorted_lst
    except ValueError as e:
        file.write(f"{description} error: {e}\n")
        return None

# Prepare the lists
list1 = [23, 104, 5, 190, 8, 7, -3]
list2 = []
list3 = [random.randint(-100000, 100000) for _ in range(1000000)]  

# File to write output
with open('sorted_results.txt', 'w') as file:
    # Write times and collect sorted lists
    sorted_lists = []
    descriptions = [
        ("List 1", list1),
        ("List 2", list2),
        ("List 3", list3)
    ]
    
    file.write("Execution Times:\n")
    for desc, lst in descriptions:
        native_result = time_and_sort(lst, sorted_list_native, f"Native function ({desc})", file)
        numpy_result = time_and_sort(lst, sorted_list_numpy, f"NumPy function ({desc})", file)
        sorted_lists.append((f"Native function ({desc})", native_result))
        sorted_lists.append((f"NumPy function ({desc})", numpy_result))
    
    # Write sorted lists
    file.write("\nSorted Lists:\n")
    for desc, sorted_lst in sorted_lists:
        if sorted_lst is not None:
            file.write(f"{desc} Sorted List: {sorted_lst}\n")
