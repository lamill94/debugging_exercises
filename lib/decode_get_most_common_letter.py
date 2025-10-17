def get_most_common_letter(text): # text = "the roof, the roof, the roof is on fire!"
    counter = {} # empty dictionary

    for char in text:
        counter[char] = counter.get(char, 0) + 1 # first key is 't', then get the value of t (default to 0 if it doesn't exist), then add 1 
    only_letter_counter = {char: counter for char, counter in counter.items() if char.isalpha()} # added this line to filter to chars in the alphabet
    letter = sorted(only_letter_counter.items(), key = lambda item: item[1], reverse = True)[0][0] # sorted function: ITERABLE = key-value pairs in the dictionary, KEY = lambda function that takes the key-value pair as an argument and returns the value (as it's index 1), reverse = True puts it in descending order. Then first index 0 gets the first key-value pair, and the second index 0 gets the key e.g. the letter
    return letter

print(f"""
Running: get_most_common_letter("the roof, the roof, the roof is on fire!")
Expected: o
Actual: {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")

