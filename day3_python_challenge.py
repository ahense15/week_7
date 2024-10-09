# Gets user input
text = input("Write any text that you want. It can be a article, sentence, poem, whatever you want: ").lower()
letter1 = input("Pick a random letter: ").lower()
letter2 = input("Pick another letter: ").lower()
letter3 = input("Pick another letter: ").lower()

# Counts the letters that the user chose
lettercount1 = (text.count(letter1))
lettercount2 = (text.count(letter2))
lettercount3 = (text.count(letter3))

# Prints the final result
print(f"You have\n{lettercount1} {letter1}'s\n{lettercount2} {letter2}'s\n{lettercount3} {letter3}'s")

# Adding a list
input_text_list = list(text)

# Finding word count
text_word_count = (len(text)) 
print(f"The word count of your text is {text_word_count}.")

# Finding first and last letter 

first_letter = (text[0])
last_letter = (text[-1])
print(f"Your first letter is {first_letter} and your last letter is {last_letter}.")

#inverted text
inverted_text = (text[::-1])
print(inverted_text)

# finding python

hasPython = "python" in text
if hasPython is True:
    print("Your text has python in it.")
else:
    print("Your text does not have python.")