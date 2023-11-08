n = int(input("Enter the number of 4-letter prompts: "))
word = []

for i in range(n):
    prompt = input(f"Enter prompt {i + 1}: ")
    if len(prompt) != 4:
        print("Prompt must be 4 letters long. Please try again.")
        exit(1)
    word.append(prompt)

common_elements = []
final_word = ''
other_words = []

for i in range(len(word) - 1):
    for j in range(len(word[0])):
        if word[i][j:] == word[i + 1][:-j]:
            common_elements.append(word[i][j:])
            final_word = word[i][:-len(word[i][j:])] + ''.join(common_elements)
            break

for w in word:
    if w not in final_word:
        other_words.append(w)

print("\nCommon Elements:", common_elements)
print("Final Word:", final_word)
for other in other_words:
    print("Other Word:", other)
