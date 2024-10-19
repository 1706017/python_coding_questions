vowel = ['a','e','i','o','u']

word = 'amrit'

count = 0

for character in word:
    if character in vowel:
        count = count + 1
        print("Vowels characters are ",character)
print("count is ",count)

