all_student=[]
for i in range(1,31):
    all_student.append(i)

student_list=[]

for i in range(28):
    student=int(input())
    student_list.append(student)

for x in student_list:
    all_student.remove(x)

for i in all_student:
    print(i)