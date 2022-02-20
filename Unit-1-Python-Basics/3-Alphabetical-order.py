"""
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters
occur in alphabetical order.

s = 'azcbobobegghakl'
"""


result = ""
longest = ""
last_index = 0

for i in range(1, len(s)):
    if s[i] >= s[i-1]:
        longest += s[i-1]
        if len(longest) > len(result):
            result = longest
            last_index = i
    else:
        longest = ""
        
result += s[last_index]
print("Longest substring in alphabetical order is:", result)
