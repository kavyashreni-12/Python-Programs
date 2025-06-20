def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the element is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
arr = [5, 2, 9, 1, 5, 6]
print("Original array:", arr)
bubble_sort(arr)
print("Sorted array:", arr)
