# 문자열 압축
# 난이도 1.5
# 시간제한 1초
# 메모리 제한 128MB

def solution(s: str):
    n = len(s)
    zip = s # 압축된 문자열
    #0~n-1
    sliced_array = []
    for slice_size in range(1,n//2):
        sliced_num = n//slice_size
        for i in range(sliced_num+1):
            sliced_array.append(s[slice_size*i:slice_size*(i+1)])

    for part in sliced_array:
        print(part, end="")
        if part == None:
            print()
            


solution("aabbaccc")