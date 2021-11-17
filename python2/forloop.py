arr_student_name=['john ClEEse','Eric IDLE','michael']
#arr_student_name.append('Rosy')
#arr_student_name[2]='Rihan'
lst_new_stu=(input("enter names: "))
#lst_spl= list(str(name_lst) for name_lst in lst_new_stu.strip().split(','))-- comprehension for loop
lst_spl=lst_new_stu.split(',')
for new_stu in lst_spl:
    arr_student_name.append(new_stu)
new_lst=list()
#print(arr_student_name)
for name in arr_student_name:
    print(name.title())

