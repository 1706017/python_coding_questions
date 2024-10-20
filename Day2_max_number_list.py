my_list = [12,13,78,89,28,90,67,99,67]

max_num = my_list[0]

for num in my_list:
    if num > max_num:
        max_num = num
    else:
        continue

print("Maximum number in the List is ",max_num)

