def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        print array[0]
        less = [i for i in array[1:] if i <= pivot]
        print less
        grater = [i for i in array[1:] if i > pivot]
        print grater
        return quicksort(less) + [pivot] + quicksort(grater)

print quicksort([10,32,21,1,2,3,4,6,31,7,21,11,70])
