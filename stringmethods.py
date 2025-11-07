def strings ():
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