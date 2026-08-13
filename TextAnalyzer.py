print("=" * 45)
print("============TEXT ANALYZER TOOL============\n")
print("=" * 45)

paragraph = input("Enter a paragraph:\n")

total_length = len(paragraph)

print("\n----- Basic Info -----")
print("Total characters (including spaces):", total_length)

if total_length > 0:
    print("First 10 characters (slicing)      :", paragraph[0:10])
    print("Last 10 characters (slicing)       :", paragraph[-10:])
    print("Reversed paragraph (slicing)       :", paragraph[::-1])
else:
    print("First 10 characters (slicing)      : No text entered")
    print("Last 10 characters (slicing)       : No text entered")
    print("Reversed paragraph (slicing)       : No text entere")

vowel_count = 0
space_count = 0
consonant_count = 0
digit_count = 0
other_count = 0

vowels = "aeiouAEIOU"

for i in range(len(paragraph)):
    ch = paragraph[i]

    if ch == " ":
        space_count += 1

    elif ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

    elif ch.isdigit():
        digit_count += 1

    else:
        other_count += 1 

words = paragraph.split()
word_count = len(words)

print("\n************Character Analysis*************\n")
print("Total Vowels      :", vowel_count)
print("Total Consonants  :", consonant_count)
print("Total Spaces      :", space_count)
print("Total Digits      :", digit_count)
print("Other Characters  :", other_count, "(punctuation/symbols)")

print("\n========== Word Analysis =========\n")
print("Total Words       :", word_count)

if word_count > 0:
    print("First Word        :", words[0])
    print("Last Word         :", words[-1])
else:
    print("First Word        : No words")
    print("Last Word         : No words")

print("\n============Word List (Traversal)==========\n")

for i in range(len(words)):
    print(f"Word {i + 1}: {words[i]}")

print("=" * 45)
print("           ANALYSIS COMPLETE")
print("=" * 45)