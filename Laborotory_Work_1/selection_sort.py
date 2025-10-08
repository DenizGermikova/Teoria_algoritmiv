def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3
    return arr, comparisons, assignments


# Варіант №25
arr = [11, 42, 67, 55, 65, 78, 25, 50, 69]
sorted_arr, comps, assigns = selection_sort(arr.copy())
print("Оригінальний список:", arr)
print("Відсортований список:", sorted_arr)
print("Кількість порівнянь:", comps)
print("Кількість присвоєнь:", assigns)
