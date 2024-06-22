# Star Program
stars = int(input("Number_of_Stars_Required :"))
for x in range(stars):
    for j in range(x+1):
        print("*", end="")
    print()

# Palindrome of String

str = input("Enter palindrome: ")
m = [True if str[::-1] == str else False]
print(m)

# String Reverse
print(str[::-1])
new_list = ""
for x in str:
    new_list = x+new_list
print(new_list)
rev = "".join((reversed(str)))
print(rev)

# Count vowels and consonants in a String
string = "GeekforGeeks!"
vowels = "aeiouAEIOU"

count = sum(string.count(vowel) for vowel in vowels)
print(count)

# Anagrams

s1 = "silent"
s2 = "listen"
s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()
if len(s1) != len(s2):
    print(f'"{s1}" and "{s2}" are not anagrams.')
else:
    sorted(s1) == sorted(s2)
    print(f'"{s1}" and "{s2}" are anagrams.')

