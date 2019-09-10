#/usr/bin/env checkio --domain=py run most-wanted-letter

# You are given a text, which contains different english letters and punctuation symbols.    You should find the most frequent letter in the text. The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter, so for the purpose of your search,    "A" == "a".    Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
# 
# If you havetwo or more letters with the same frequency,    then return the letter which comes first in the latin alphabet.    For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
# 
# Input:A text for analysis as a string.
# 
# Output:The most frequent letter in lower case as a string.
# 
# Precondition:
# A text contains only ASCII symbols.
# 0 < len(text) ≤ 105
# 
# 
# END_DESC
#
# Input: A text with letters, symbols and whitespaces.
# Output: The most frequent letter in lower case OR the letters tha comes first in the alphabet in case of the same frequency. 
# Constraints: 
def checkio(text: str) -> str:
    # algorithm 
    # Create variable mostFrequentyLetter
    # Create a hashtable <letter,frequency>
    # For each letter in the text
    #  Check if it is not a symbol
    #   Convert the letter to lowercase
    #    Get the frequency for letter from hashtable
    #    If there is a frequency
    #     Increment the frequency and update the hashtable
    #     -> Get the mfrequency for mostFrequentLetter
    #     -> If frequency > mFrequency then
    #         mostFrequentyLetter receives letter
    #        Else if frequency == mFrequency then
    #         if letter is first in the alphabet than mostFrequentLetter then
    #            mostFrequentLetter receives letter
    #    When there is no frequency for letter
    #     add letter to hashtable with frequency 1
	#     if mostFrequentyLetter has no value
	#	   mostFrequentyLetter receives letter
	#     When there exists mostFrequentyLetter
	#      Get the mFrequency from mostFrequentyLetter
	#      If mFrequeny is 1 and letter is first in the alphabet than mostFrequentLetter then
	#       mostFrequntyLetter receives letter
    # return mostFrequentLetter
    
    
    # Create variable mostFrequentyLetter
    mostFrequentyLetter = None
    # Create a hashtable <letter,frequency>
    hashTable = {}
    # For each letter in the text
    for letter in text:
    #  Check if it is not a symbol
        if ((letter.isalpha() or letter.isnumeric()) and not letter.isspace()):
    #   Convert the letter to lowercase
         letter = letter.lower()
    #    Get the frequency for letter from hashtable
         frequency = hashTable.get(letter)
    #    If there is a frequency
         if frequency:
    #     Increment the frequency and update the hashtable
          frequency += 1
          hashTable[letter] = frequency
    #     -> Get the mfrequency for mostFrequentLetter
          mFrequency = hashTable[mostFrequentyLetter]
    #     -> If frequency > mFrequency then
          if (frequency > mFrequency):
    #       -> mostFrequentyLetter receives letter
            mostFrequentyLetter = letter
    #        Else if frequency == mFrequency then
          elif (frequency == mFrequency):
    #        -> if letter is first in the alphabet than mostFrequentLetter then
            if (ord(letter) < ord(mostFrequentyLetter)):
    #            -> mostFrequentLetter receives letter
                mostFrequentyLetter = letter
    #    When there is no frequency for letter
         else:
    #    -> add letter to hashtable with frequency 1
          hashTable[letter] = 1
    #     -> if mostFrequentyLetter has no value 
          if not mostFrequentyLetter:
    #     -> mostFrequentyLetter receives letter
           mostFrequentyLetter = letter
    #     When exists mostFrequentyLetter       
          else:
    #         Get the mFrequency from mostFrequentyLetter
              mFrequency = hashTable[mostFrequentyLetter]
    #         If mFrequeny is 1 and letter is first in the alphabet than mostFrequentLetter then
              if mFrequency == 1 and (ord(letter) < ord(mostFrequentyLetter)):
    #             mostFrequntyLetter receives letter
                  mostFrequentyLetter = letter

    # return mostFrequentLetter
    return mostFrequentyLetter

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
