# Count vowels and consonants

s = input("Enter a string: ").lower()

vowels = 0
consonants = 0

for ch in s:
    if ch.isalpha():   # Check only alphabets
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Number of vowels =", vowels)
print("Number of consonants =", consonants)
