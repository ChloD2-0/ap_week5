# a function allows us to bundle code into
# reusable blocks, making it easier to manahe 
# and understnad. By defining functions, we can
# avoid code duplication and enhance readability

# define a function
def problem1(): 
    # pass # I put pass here to avoid syntax error

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
    # calling a function
