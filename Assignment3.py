def SelectionSort(array):
    min = 999999

    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] < array[j]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]
        print(array)




x = [66, 53, 91, 32, 73, 82, 41]
SelectionSort(x)