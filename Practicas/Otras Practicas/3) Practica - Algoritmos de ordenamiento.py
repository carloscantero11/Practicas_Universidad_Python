# Quicksort

lista = [9,13,1,2,3,6,11,17,5,12,19]

def particion(lista):

    pivot = lista[0]
    menor = []
    mayor = []

    for i in range(1,len(lista)):
        if(lista[i]<pivot):
            menor.append(lista[i])
        else:
            mayor.append(lista[i])

    return menor, pivot, mayor

def quicksort(lista):

    if(len(lista)<2):
        return lista

    menor, pivot, mayor = particion(lista)

    return quicksort(menor)+ [pivot] + quicksort(mayor)

print("------------------------Quicksort------------------------")
print(quicksort(lista),"\n")
print()

#Heapsort

def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1 
    r = 2 * i + 2
    
    if(l<n and arr[i] < arr[l]):
        largest = l

    if(r < n and arr[largest] < arr[r]):
        largest = r

    if(largest != i):
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    for i in range(n // 2-1, -1, -1):
        heapify(arr,n,i)
        
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr,i,0)

print("------------------------Heapsort-------------------------")
arr=[12,11,13,5,6,7,]
heapsort(arr)
print(arr)


#Shellsort

def shellsort(array,n):
    interval = n // 2

    while(interval>0):
        for i in range(interval,n):
            temp = array[i]
            j=i

            while(j>=interval and array[j-interval]>temp):
                array[j] = array[j-interval]
                j-=interval
            array[j] = temp
        interval//=2
print()
print("------------------------Shellsort-------------------------")
data = [9,8,3,7,5,6,4,2]
size = len(data)
shellsort(data,size)
print(data)
print()

#Hashing

def display_hash(hashtable):
    for i in range(len(hashtable)):
        print(i,end=" ")

        for j in hashtable[i]:
            print("-->",end=" ")
            print(j,end=" ")
        print()
        
hashtable = [[] for _ in range(10)]

def hashing(keyvalue):
    return keyvalue % len(hashtable)

def insert(hashtable,keyvalue,value):
    hash_key = hashing(keyvalue)
    hashtable[hash_key].append(value)
    
print("------------------------Hashing-------------------------")
insert(hashtable,1,"Hola Mundo")
insert(hashtable,9,"Dato")
insert(hashtable,5,"hola")
display_hash(hashtable)
print()

#Mergesort

def merge_sort(list):

    list_length = len(list)

    if list_length == 1:
        return list

    mid_point = list_length // 2

    left_partition = merge_sort(list[:mid_point])
    right_partition = merge_sort(list[mid_point:])

    return merge(left_partition, right_partition)

def merge(left, right):
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])

    return output


def run_merge_sort():
    unsorted_list = [4, 1, 5, 7, 2, 6, 1, 1, 6, 4, 10, 33, 5, 7, 23]
    print(unsorted_list)
    sorted_list = merge_sort(unsorted_list)
    print(sorted_list)

print("------------------------Mergesort-------------------------")
run_merge_sort()

