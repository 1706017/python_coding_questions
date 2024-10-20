my_list = [12,23,45,21,99,89,90,43]

first_max = my_list[0]

second_max = -1

for num in my_list:
    if num > first_max:
        first_max = num
    else:
        continue

print("First Largest Number is ",first_max)

for num in my_list:
    if num > second_max and num != first_max:
        second_max = num
    else:
        continue

print("Second Largest Number is",second_max)
