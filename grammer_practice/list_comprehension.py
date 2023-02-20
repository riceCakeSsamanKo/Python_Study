# 홀수로 구성된 리스트 초기화
array1 = [i for i in range(20) if i%2 == 1]
print(f"홀수로 구성된 리스트 {array1}")

# 제곱수로 구성된 리스트 초기화
array2 = [(i+1)**2 for i in range(5)]
print(f"제곱수로 구성된 리스트 {array2}")

# 3의 배수로 구성된 리스트 초기화
array3 = [i for i in range(30) if i%3==0]
print(f'3의 배수로 구성된 리스트 {array3}')

# 크기가 10인 0으로 초기화 된 1차원 리스트
array4 = [0]*5
print(f"크기가 5인 0으로 초기화 된 1차원 리스트 {array4}")

# 3*5 크기의 0으로 초기화 된 2차원 리스트 초기화
array5 = [[0]*5 for _ in range(3)]
print(f"3*5 크기의 0으로 초기화 된 2차원 리스트 초기화 {array5}")

# row가 증가함에 따라 원소 개수가 증가하는 2차원 리스트
array6 = [[i+1]*(i+1) for i in range(3)]
print(f"row가 증가함에 따라 원소 개수가 증가하는 2차원 리스트 {array6}")


