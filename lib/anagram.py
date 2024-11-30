# your code goes here!

class Anagram:
    """
    A class to find anagrams of a given word from a list of possible words.
    """

    def __init__(self, word):
        """
        Initialize the Anagram object with a word.
        :param word: The word to match anagrams against.
        """
        # Normalize the input word by lowercasing and sorting its letters
        self.word = word.lower()
        self.sorted_word = sorted(self.word)  # Sorted list of letters

    def match(self, candidates):
        """
        Find all anagrams of the word in the given list of candidates.
        :param candidates: List of words to check for anagrams.
        :return: List of anagrams.
        """
        matches = []  # List to store matching anagrams

        # Iterate over each candidate word
        for candidate in candidates:
            # Skip if candidate is the same as the word itself
            if candidate.lower() == self.word:
                continue

            # Normalize candidate by sorting letters
            if sorted(candidate.lower()) == self.sorted_word:
                matches.append(candidate)  # Add to matches if it is an anagram

        return matches
