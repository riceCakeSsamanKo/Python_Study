students = [90,80,89,46,39,76,94,100,81]
blackList = [2,4]

for i in range(len(students)):
    if i in blackList:
        print(f"{i+1}번 학생은 블랙 리스트이다")
        continue

    if (students[i] >= 80):
        print(f"{i + 1}번 학생은 80점 이상이다")
    else:
        print(f"{i + 1}번 학생은 80점 이하이다")

