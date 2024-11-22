import unittest

from project1 import FrequentlyUsedWords

class TestFrequentlyUsedWords(unittest.TestCase):

    def test_word_count(self):
        """Test that word count increments when a word is read in."""
        frequentlyUsedWords = FrequentlyUsedWords()

        wordCount = frequentlyUsedWords.wordCounts.get('test')
        wordCount = 0 if wordCount is None else wordCount

        self.assertEqual(wordCount, 0) # test that the word counts have been initialised as empty

        frequentlyUsedWords.readWord('test') # test reading a word for the first time

        self.assertEqual(frequentlyUsedWords.wordCounts.get('test'), 1)

        frequentlyUsedWords.readWord('test') # test reading a word that has been seen previously

        self.assertEqual(frequentlyUsedWords.wordCounts.get('test'), 2)

    def test_most_used_words(self):
        """Test geting the most frequently used words."""

        frequentlyUsedWords = FrequentlyUsedWords()

        # Lorem text generated using https://www.lipsum.com/
        with open('lorem.txt', 'r') as f:
            try:
                text_string = f.read()
            except:
                text_string = ''

        # Remove all punctuation
        text_string = text_string.translate({
            ord(','): '',
            ord('.'): ''
        })

        # Most frequent words were obtained using http://www.writewords.org.uk/word_count.asp
        expectedFrequentWords = ['sit', 'amet', 'in', 'vitae', 'sed', 'eros', 'lorem', 'suspendisse', 'non', 'vestibulum']

        # Read in text word by word
        for word in text_string.split():
            frequentlyUsedWords.readWord(word)

        # Test default value of 10
        mostFrequentWords = frequentlyUsedWords.getFrequentlyUsedWords()
        
        # We compare sets since multiple words can have the same frequency, so the order in which they are listed is ambiguous and may be different
        self.assertEqual(set(expectedFrequentWords), set(mostFrequentWords))

        # Test a different value for n
        mostFrequentWords = frequentlyUsedWords.getFrequentlyUsedWords(6)
        self.assertEqual(set(expectedFrequentWords[:6]),set(mostFrequentWords))

if __name__ == "__main__":
    unittest.main()