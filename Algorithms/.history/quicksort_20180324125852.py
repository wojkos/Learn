import random

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        grater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(grater)

arr = []

for _ in range(5000000):
    arr.append(random.randrange(0,100000))

print quicksort(arr)
