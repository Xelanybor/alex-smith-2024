class FrequentlyUsedWords():
    """A class that reads words one at a time from a string of text and keeps track of how frequently each word is used, as well as the most frequently used words."""

    def __init__(self):
        
        # Keeps track of how many times each word has been seen
        self.wordCounts: dict[str, int] = {}

        # All words in descending order of their frequency
        self.words = []

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
            self.words.remove(word)
        else:
            self.wordCounts[word] = 1
        
        self.__insertWord(word)

    def __insertWord(self, word: str):
        """Insert a word into the internal word list, in the correct position based on its frequency.

        Args:
            word (str): Word to be inserted into the internal word list.
        """

        # If the word list is already empty, just append the current word
        if len(self.words) == 0:
            self.words.append(word)
            return

        currentWordCount = self.wordCounts[word]

        # Do a basic binary search to find where to insert the word

        left, right = 0, len(self.words) - 1

        while left <= right:
            mid = (left + right) // 2

            # Since we don't care about the order of words with the same count, we can insert our word next to any other word with the same frequency
            if self.wordCounts[self.words[mid]] == currentWordCount:
                left = mid
                break
            # Otherwise keep narrowing the search area as is typical for binary search
            elif self.wordCounts[self.words[mid]] >= currentWordCount:
                left = mid + 1
            else:
                right = mid - 1
        
        self.words.insert(left, word)



    def getFrequentlyUsedWords(self, n: int = 10) -> list[str]:
        """Get the top n most frequently used words.

        Args:
            n (int, optional): How many most frequently words to get. Defaults to 10.

        Returns:
            list[str]: A list of the top n most frequently used words.
        """

        # # Return a maximum of n frequently used words, or fewer if there aren't that many words
        return self.words if len(self.words) <= n else self.words[:n]
    
if __name__ == '__main__':

    # CLI to demonstrate usage of the class
    print("Question 1: Frequently Used Words")
    print("=================================")

    userInput = input("Enter a string of text to analyse, or (q) to quit:\n> ")

    # Loops until the user enters 'q' as input
    while userInput != 'q':
        frequentlyUsedWords = FrequentlyUsedWords()
        
        # Assuming the user enters a valid input with no punctuation since input validation is out of scope for this question
        for word in userInput.split():
            frequentlyUsedWords.readWord(word)

        # Output the most frequently used words in order of their frequency
        print("---------------------------------")
        print("Most frequently used words:")
        mostFrequentlyUsedWords = frequentlyUsedWords.getFrequentlyUsedWords()
        for i, word in enumerate(mostFrequentlyUsedWords):
            print(f"{i + 1:>2}) {word} : {frequentlyUsedWords.wordCounts[word]}")

        print("=================================")

        userInput = input("Enter a string of text to analyse, or (q) to quit:\n> ")