def bubble_sort(values):
    size = len(values)
    if size <= 1:
        return values
    else:
        for i in range(size):
            for j in range(0,size-i-1):
                if values[j]>values[j+1]:
                    aux = values[j+1]
                    values[j+1] = values[j]
                    values[j] = aux
        return values

def sort_selection(values, k):
    values = bubble_sort(values)
    return values[k-1]