my_lst = [12,13,14,39,90]

flag_check = False
len_my_list = len(my_lst)

for i in range(0,len_my_list-1):
    if my_lst[i] <= my_lst[i + 1]:
        continue
    else:
        flag_check = True

if flag_check == False:
    print("The List is Sorted")
else:
    print("The List is not Sorted")
    
