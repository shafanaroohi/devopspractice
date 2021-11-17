arr_guest_name=['john ClEEse','Eric IDLE','michael']
arr_guest_name1 = ['graHam chapman', 'TERRY', 'terry jones']
# add two names to the list and send invitation to all

msg='You are invited to the party tonight!!'
arr_guest_name.extend(arr_guest_name1)
print("Party Invitation")
#arr_student_name.append('Rosy')
lst_new_stu=(input("enter names: "))
#lst_spl= list(str(name_lst) for name_lst in lst_new_stu.strip().split(','))-- comprehension for loop
lst_spl=lst_new_stu.split(',')
for new_stu in lst_spl:
    arr_guest_name.append(new_stu)
    #new_lst=list()
#print(arr_student_name)
for names in arr_guest_name:
     print(f'{names.title()} {msg}')

