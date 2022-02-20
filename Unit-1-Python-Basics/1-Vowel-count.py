"""
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

s = 'azcbobobegghakl'
"""

vowels = "aeiou"
vowel_count = 0

for i in s:
    if i in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)
