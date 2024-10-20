str1 = input("Enter a string to check if it is palindrome or not")

rev_str = str1[::-1]

if str1 == rev_str:
    print("String is palindrome")
else:
    print("String is not palindrome")

