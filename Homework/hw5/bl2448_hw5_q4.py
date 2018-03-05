word=input("Enter a world: ")
word=word.lower()
vowel_count=0
consonant_count=0
vowels="aeiou"
for letter in range(len(word)):
	if (vowels.find(word[letter]) != -1):
		vowel_count+=1
	else:
		consonant_count+=1
print(word, "has", vowel_count, "vowels and", consonant_count, "consonants.")
