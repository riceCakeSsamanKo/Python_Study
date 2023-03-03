# 성적이 낮은 순서로 학생 출력하기
# 난이도 1
# 시간 제한 1초
# 메모리 제한 128MB

n = int(input())
array = []
for i in range(n):
    input_data = input().split()  # split하면 list가 반환됨
    array.append((input_data[0],int(input_data[1])))

#sorted는 비파괴적 함수임(sort는 파괴적)
array = sorted(array, key = lambda data: data[1]) # lambda식을 이용해 2번째 요소를 기준으로 sort

for student in array:
    print(student[0])



