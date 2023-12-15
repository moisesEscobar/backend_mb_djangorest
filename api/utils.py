def sorting_algorithm(lst, key=lambda x: x):
    # Caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(lst) <= 1:
        return lst

    # Seleccionar un elemento como pivote (en este caso, el del medio)
    pivot = lst[len(lst) // 2]

    # Dividir la lista en elementos menores, iguales y mayores que el pivote
    left = [item for item in lst if key(item) < key(pivot)]
    middle = [item for item in lst if key(item) == key(pivot)]
    right = [item for item in lst if key(item) > key(pivot)]

    # Recursivamente ordenar las sublistas
    left_sorted = sorting_algorithm(left, key)
    right_sorted = sorting_algorithm(right, key)

    # Concatenar las sublistas ordenadas y el elemento igual al pivote
    return left_sorted + middle + right_sorted