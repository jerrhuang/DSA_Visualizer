from engine.events import Compare, Swap

def bubble_sort(values):
    events = []
    arr = values.copy()
    
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            events.append(Compare(j, j + 1))
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                events.append(Swap(j, j + 1))
    
    return events