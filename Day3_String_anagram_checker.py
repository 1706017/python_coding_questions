#String Anagram has to satisfy below two Conditions
#1.Length of both the strings should be same
#2.Characters in both the string should be same either in same order or
# different Order 

#Exmaple: ABC AND CAB ARE string anagrams

str1 = input("Enter String1")
str2 = input("Enter String2")

if len(str1)!= len(str2):
    print("Not Anagram strings")
else:
    if sorted(str1) == sorted(str2):
        print("Strings are Anagrams")
    else:
        print("String are not anagrams")

    
