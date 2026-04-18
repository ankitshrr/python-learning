vowel = "AEIOU"
s = "ankit"
count = 0
for ch in s:
    if ch in vowel.lower():
        count += 1

print(count)
co=sum(ch in "aeiou"for ch in s)