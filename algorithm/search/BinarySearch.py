def binarySearch(array,target,start,end):
    while start<=end:
        mid = (start+end)//2
        if array[mid] == array[target]:
            return mid
        elif array[mid] > array[target]:
            end = mid - 1
        else:
            start = mid+1