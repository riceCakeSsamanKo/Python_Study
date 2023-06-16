import heapq

def heap_sort(array:list, sort_type:int):
    # sort_type == 0 -> minheap
    # sort_type == 1 -> maxheap

    if isinstance(array,list) is not True:
        print("please input right value. list")
        return False

    heap = []
    result = []

    if sort_type == 0:
        for value in array:
            heapq.heappush(heap,value)
        for _ in range(len(array)):
            result.append(heapq.heappop(heap))

    elif sort_type == 1:
        for value in array:
            heapq.heappush(heap,-value)
        for _ in range(len(array)):
            result.append(-heapq.heappop(heap))

    else:
        print("error! please enter the right input")
        return False


    return result


sort_type = int(input("<please enter the sort type>\n(min: 0, max: 1) >>>"))
array = [253,212,64,21,93,77,346,-12,401,55,-27,64,-92]

sort = heap_sort(array, sort_type)
print(sort)
