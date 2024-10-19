vowel = ['a','e','i','o','u']

word = 'amrit'

count = 0

for character in word:
  if character not in vowel:
    count = count + 1

print("Number of consonant in word is",count)

