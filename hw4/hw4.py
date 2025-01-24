"""
CMSC 14100
Winter 2025
Homework #4

We will be using anonymous grading, so please do NOT include your name
in this file

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URL of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

# Global constants
PUNCTUATION = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


# Exercise 1
def compress_word(word):
    """
    Given a word, produce a compressed version of the word, by stripping all
    interior vowels.

    Input:
        word (str): text to be compressed

    Output (str): compressed word without interior vowels
    """
    ### YOUR CODE HERE


# Exercise 2
def segment_text(text, seq):
    """
    Given a text and a binary sequence, segment the text into words according
    to the sequence.

    Input:
        text (str): the text to be segmented
        seq (str): binary sequence representing the locations of words

    Output (list[str]): list of words comprising the text
    """
    ### YOUR CODE HERE


# Exercise 3
def count_words(wordlist, text):
    """
    Given a list of words and a text, produce a count of the occurrences of
    each word from the word list in the text.

    Input:
        wordlist (list[str]): list of words to be counted
        text (str): text to search

    Output (list[tuple[str,int]]): list of (word, count) pairs
    """
    ### YOUR CODE HERE

# Exercise 4
def list_bigrams(text):
    """
    Given a text, produce a list of all bigrams contained in the text, in the
    order that they appear.

    Input:
        text (str): the text

    Output (list[tuple[str,str]]): list of bigrams contained in text
    """
    ### YOUR CODE HERE

# Exercise 5
def term_frequency(counts):
    """
    Given a list of (word, count) pairs, produce a list of (count, word) pairs,
    ordered from greatest to least, then lexicographically.

    Input:
        counts (list[tuple[str,int]]): list of (word, count) pairs

    Output (list[tuple[int,str]]): sorted list of (count, word) pairs
    """
    ### YOUR CODE HERE


# Exercise 6
def sentiment_score(pos, neg, text):
    """
    Given a list of positive words, a list of negative words, and a text,
    produce a sentiment score based on the number of occurrences of the given
    words in the text.

    Each occurrence of a "positive" word contributes +1 to the score and each
    "negative" word contributes -1 to the score.

    Input:
        pos (list[str]): list of positive words
        neg (list[str]): list of negative words
        text (str): the text

    Output (int): sentiment score for the text
    """
    ### YOUR CODE HERE


# Exercise 7
def str_to_sentences(abbr, text):
    """
    Given a list of abbreviations and a text, produce a list containing the 
    sentences of the text, in order. A sentence is a sequence of words that 
    ends in one of the following punctuation marks: ".", "!", "?". Sentences
    should not end on any of the given abbreviations.

    Input:
        abbr (list[str]): list of abbreviations
        text (str): the text to be broken up

    Output (list[str]): list of sentences that comprise text
    """
    ### YOUR CODE HERE


# Exercise 8
def dale_chall(easy, text):
    """
    Given a list of "easy" words and a text, compute the Dale-Chall readability
    score for the text, relative to the list of easy words.

    Input:
        easy (list[str]): list of easy words
        text (str): the text to be analyzed

    Output (float): Dale-Chall readability score for the text
    """
    ### YOUR CODE HERE


