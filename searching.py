import random
import time

# Fungsi Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result

# Fungsi Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Generate 100 bilangan acak
arr_merge = [random.randint(0, 1000) for _ in range(100)]
arr_bubble = [random.randint(0, 1000) for _ in range(100)]

#untuk bubble
start_time_bubble_sort = time.perf_counter()
bubble_sorted = bubble_sort(arr_bubble)
end_time_bubble_sort = time.perf_counter()
time_complexity_bubble = end_time_bubble_sort - start_time_bubble_sort

#untuk merge
start_time_merge_sort = time.perf_counter()
merge_sorted = merge_sort(arr_merge)
end_time_merge_sort = time.perf_counter()
time_complexity_merge = end_time_merge_sort - start_time_merge_sort

print(f"Time Complexity untuk Bubble Sort {time_complexity_bubble:.10f} detik \n")
print(f"Time Complexity untuk Merge Sort  {time_complexity_merge:.10f} detik \n")
