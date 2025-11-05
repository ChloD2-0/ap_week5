# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string 
magic = "abracadabra"
# a. Retrieve the 5th character.
# b. Retrieve the second to last character.
# c. Find the first occurrence of the letter 'c'.
fifth_char = magic[4]
print(fifth_char)
tenth_char = magic[9]
print(tenth_char)
char_to_find = "c" 
index = magic.find(char_to_find)
if index != -1: 
    print(f"The first occurence of {char_to_find}, is at index {index} ") 
else:
    print("'{char_to_find}'not found in the string.")
    


# Advanced Slicing:
# Given the string 
alphabet = "abcdefghijklmnopqrstuvwxyz"
# a. Extract the letters 'hij'.
# b. Extract every second letter starting from 'a' to 'm'.
# c. Reverse the entire string using slicin
hij = alphabet[7:10]
print(hij)
print(alphabet [::-1])



# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the 
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(len(quote))
print(quote [83:98])

# Manipulating Words:
# Given the string 
info = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
words = info.split() [::3]
print(info [::-1])

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: 
text = "MAY THE FORCE BE WITH YOU" 
lowercase_text = text.lower()
print(lowercase_text)

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."]
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.
motto = ["Make", "haste", "slowly."]
motto_string = ' '.join(motto)
print(motto_string)
               
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
sentence = "Life is what happens when you are busy making other plans."
mod_sentence = sentence.replace("busy", "distracted").replace("plans" , "mistakes")
print(mod_sentence) 
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
word = "Iternation" 
# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
word = "moonlight" 
quote =  "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
appears_in_quote = word in quote
print(appears_in_quote)
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/
phrase = "Supercalifragilisticexpialidocious"
# b. Count the number of times the letter 'i' appears in the same word/phrase.
print(len(phrase))
count_of_i = phrase.count('i') 
print(count_of_i) 