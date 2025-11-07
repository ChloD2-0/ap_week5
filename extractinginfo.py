def extracting_info():
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