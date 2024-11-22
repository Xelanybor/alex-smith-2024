class FrequentlyUsedWords():
    """Reads words one at a time from a string of text and keeps track of how frequently each word is used, as well as the most frequently used words."""

    wordCounts: dict[str, int] = {}

    def __init__(self):
        pass

    def readWord(self, word: str):
        """Read one word from the input string and update the corresponding word count.

        Args:
            word (str): The current word being read from the input string.
        """

        # Make the method case insensitive
        word = word.lower()
        
        # Update the stored word counts
        if word in self.wordCounts:
            self.wordCounts[word] += 1
        else:
            self.wordCounts[word] = 1

    def getFrequentlyUsedWords(self, n: int = 10) -> list[str]:
        """Get the top n most frequently used words.

        Args:
            n (int, optional): How many most frequently words to get. Defaults to 10.

        Returns:
            list[str]: A list of the top n most frequently used words.
        """

        # Get list of words that have been seen
        words = list(self.wordCounts.keys())

        # Sort the word list by their frequency
        words.sort(key = lambda word : self.wordCounts.get(word), reverse=True)

        # Return a maximum of n frequently used words, or fewer if there aren't that many words
        return words if len(words) <= n else words[:n]