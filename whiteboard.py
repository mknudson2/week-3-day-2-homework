# You need to write a function, that returns the first non-repeated character in the given string.

# If all the characters are unique, return the first character of the string.
# If there is no unique character, return None.

# You can assume, that the input string has always non-zero length.

# Examples
# "test"   returns "e"
# "teeter" returns "r"
# "trend"  returns "t" (all the characters are unique)
# "aabbcc" returns None (all the characters are repeated)


"""
Reqs:
1. find how often each letter occurs in a given string
2. find the first letter in the string that only occurs once

Steps:
1. use a for loop to loop through the entire string
2. create a dictionary to store the key:value pairs of character(key) and its frequency(value)
3. create a conditional: if it occurs more than once, incriment, otherwise, its value is 1 (since it occurs once)
4. loop through the established dictionary to find the first character with the value of 1
5. that character is the first letter to uniquely occur
6. if no character fits that criteria, return none
"""                      


def first_unique_char(string):
    char_count = {}
    string = string.lower()
    # Count the amount of times each character appears
    for char in string: #for each character in the input 'string'
        if char in char_count: #conditional: store characters in the char_count dictionary and increase the number 
            char_count[char] += 1 #incriment for each instance of that char appearing in the string 
        else: 
            char_count[char] = 1 #however, if the character only occurs once, then the count will be 1.
    
    # Find the first non-repeated character
    for char in string: #once we have our dictionary with the key:value pairs of char:occurence, we will loop through it to find the first value equal to 1
        if char_count[char] == 1: #since the character keys were put in order from beginning to end, the values are associated with their occurance, for example in the string test, the dictionary would look like {t: 2, e: 1, s: 1}. Looping through this dictionary reveals the first character to be unique is 'e' since it is the first character whose value is equal to 1.
            return char 
    
    return None  # however, if no characters are unique/non-repeated, then there is nothing to count, so we will return none.


print(first_unique_char("test"))
print(first_unique_char("teeter"))
print(first_unique_char("trend"))
print(first_unique_char("aabbcc"))


"""
Ben Copen's Solution
"""

def uniquechar(word):
    word = word.lower()
    for char in word:
        count = 0
        for item in word:
            if char == item:
                count += 1
            if count == 1:
                return char
    return None

        
"""
Ben Deitch's Solution
"""
def count(string):
    string = string.lower*()
    for character in string:
        if string.count(character)==1:
            return character
    return None


"""
Christian Gould's Solution
"""
#same as mine, just different variable names


"""
Dylan's Solution 1
"""

def find_first_unique(astring):
    letter_hash = {}
    for letter in astring:
        letter_hash[letter] = letter_has.get(letter, 0) + 1
        if letter...
