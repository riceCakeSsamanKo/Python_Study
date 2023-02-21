array_list = [1,2,3,4,5]
array_tuple = (1,2,3,4,5)

print(f"list {array_list}")
print(f"tuple {array_tuple}")

# tuple은 값 변경 불가
# array_tuple[1] = 30  => error

array = [(1,2), (3,4), (5,6)]
for tuple in array:
    print(tuple[1])