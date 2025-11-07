# refactoring means to 
# restrucutre code wihtout 
# changing its external behavior
# This help improve code readability
# and maintainabilitiy. 


# importing the functions
from problem_set1 import problem1
from advanced_slicing import advanced_slice
from extractinginfo import extracting_info 
from advstrings_props import advanced_operations

#call the functions
problem1()
advanced_slice()
extracting_info()
advanced_operations() # this is 
# an abstraction representation
# of the function




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
find_word = "subjective"
search_word = info.find("subjective")
if "subjective" in info:
    print((find_word))
else:
    print("Word not in the text.")

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

