import numpy as np
import time
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def ternary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        if arr[mid1] == target:
            return mid1
        elif arr[mid2] == target:
            return mid2
        elif arr[mid1] > target:
            high = mid1 - 1
        elif arr[mid2] < target:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    return -1

# ARRAY ARRAY ARRAY ARRAY ARRAY ARRAY ARRAY
n = 1000
X = np.random.randint(0, 1000, size=n)
print("Original array:", X)

# Mergesort
start_time = time.time()
merge_sorted_X = merge_sort(X.copy())
merge_sort_time = time.time() - start_time
print("Mergesort result:", merge_sorted_X)

# Quicksort
start_time = time.time()
quick_sorted_X = quicksort(X.copy())
quick_sort_time = time.time() - start_time
print("Quicksort result:", quick_sorted_X)

# Binario
target = np.random.choice(X)
start_time = time.time()
binary_search_result = binary_search(merge_sorted_X, target)
binary_search_time = time.time() - start_time
print("Binary search result index:", binary_search_result)

# Ternario
start_time = time.time()
ternary_search_result = ternary_search(merge_sorted_X, target)
ternary_search_time = time.time() - start_time
print("Ternary search result index:", ternary_search_result)
print(f"Mergesort execution time: {merge_sort_time} seconds")
print(f"Quicksort execution time: {quick_sort_time} seconds")
print(f"Binary search execution time: {binary_search_time} seconds")
print(f"Ternary search execution time: {ternary_search_time} seconds")
