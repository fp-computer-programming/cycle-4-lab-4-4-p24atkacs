"""

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a Python file named lab_4-4.py

Use the find method to return the index of the first occurrence of the letter "t" in the word "flibbertigibbet".

Using this value, print the letter immediately following the first "t". hint: you may need to store the index value as a variable!

Create a variable storing you first name written in lowercase. Using a string method, print this variable in uppercase.

Use the split method to split the following sentence at each comma: "I wish, I wish, I was a fish."

"""

# Author: Andrew Tkacs

# Finding the index of the first occurrence of 't' in the word 'flibbertigibbet'

word = "flibbertigibbet"
first_t_index = word.find('t')

# Check if 't' is found in the word and print the letter immediately following it

if first_t_index != -1 and first_t_index < len(word) - 1:
    letter_following_t = word[first_t_index + 1]
    print("Letter following the first 't':", letter_following_t)

# Storing your first name in lowercase and printing it in uppercase

first_name = "andrew"
uppercase_name = first_name.upper()
print("Uppercase Name:", uppercase_name)

# Splitting a sentence at each comma

sentence = "I wish, I wish, I was a fish."
split_sentence = sentence.split(',')
print("Split Sentence:", split_sentence)
