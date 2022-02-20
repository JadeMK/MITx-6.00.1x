"""
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.

s = 'azcbobobegghakl'
"""

bob_count = 0

for i in range(len(s) - 2):
    if s[i:i+3] == "bob":
        bob_count += 1

print("Number of times bob occurs is:", bob_count)
