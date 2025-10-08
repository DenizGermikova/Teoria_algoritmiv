def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    for i in range(1, n):
        key = arr[i]
        assignments += 1
        j = i - 1
        assignments += 1

        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
            assignments += 1

        if j >= 0:
            comparisons += 1

        arr[j + 1] = key
        assignments += 1

    return arr, comparisons, assignments


# Варіант №25
A = [11, 42, 67, 55, 65, 78, 25, 50, 69]
sorted_A, comps, assigns = insertion_sort(A.copy())
print("Оригінальний список:", A)
print("Відсортований список:", sorted_A)
print("Кількість порівнянь:", comps)
print("Кількість присвоєнь:", assigns)
