import string

def isPangram(str1: str, alphabet: str=string.ascii_lowercase) -> bool:
    """Check whether a given string is a pangram or not. A pangram is a word or sentence containing every letter of the alphabet at least once.

    Args:
        str1 (str): The string to check.
        alphabet (str, optional): Which alphabet to use. Defaults to the default English a-z alphabet (specifically `string.ascii_lowercase`).
    """

    # If there are fewer letters in the string than the alphabet, then it definitely cannot contain all letters in the alphabet
    if len(alphabet) > len(str1):
        return False
    
    str1 = str1.lower() # Convert to lowercase to make the comparison case-insensitive

    # Used to track which letters in the alphabet must still be found in the string
    # This is a dict instead of a list since dict lookup is O(1)
    # Creating this dict is O(len(alphabet))
    lettersToBeFound = {letter: True for letter in alphabet}

    # How many letters from the alphabet in the alphabet still need to be found in the string
    # This only gets decremented when a letter is found in the string for the first time (which is tracked by `lettersFound`)
    # This acts as a sort of checksum so that checking whether all letters have been found is O(1) (i.e. if lettersRemaining == 0)
    lettersRemaining = len(lettersToBeFound)

    for letter in str1:
        if lettersToBeFound.get(letter, False): # If the letter isn't in the string then it does not need to be found, so default to False
            # If the letter must still be found, then we update the "checksum" lettersRemaining value
            lettersRemaining -= 1
            # And update the dict since we no longer need to find it in the rest of the string
            lettersToBeFound[letter] = False

            # Check if we have found all of the needed letters (so that we can stop early if we have)
            # Since lettersRemaining is only updated in this loop, we only need to check in this loop
            # And this check is only O(1)
            if lettersRemaining == 0:
                return True
            
    # Otherwise if we loop through the whole string and still have letters from the alphabet that haven't been found, return False
    return False
    
print(isPangram('abcdefghijklmnopqrstuvwxyz'))