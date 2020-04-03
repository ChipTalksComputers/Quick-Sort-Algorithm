
A =[1,9,78,65,43,0,23,48]


def partition(array,low, high):
    i = low
    j = high-1
    pivot = array[i]
    while(i<j):
        while(array[i] < pivot):
            i += 1
        while(array[j] > pivot):
            j -= 1
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
    temp = pivot
    pivot = array[j]
    array[j] = temp
    
    return j


def Quick_Sort(a, low, high):
    if low!=high:
        j = partition(a, low, high)

        Quick_Sort(a, low, j)
        Quick_Sort(a, j+1, high)
    

    
Quick_Sort(A, 0, len(A))
print(A)
