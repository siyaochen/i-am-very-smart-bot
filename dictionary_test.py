from PyDictionary import PyDictionary
import praw
import time

# user_agent = "I am very smart bot 1.0"
# r = praw.Reddit(user_agent = user_agent)

# Finds the longest synonym given a word
def longest_synonym(word):
	dictionary = PyDictionary()
	synonyms = dictionary.synonym(word)
	longest = ""

	max_length = 0
	if synonyms is not None: # If synonyms are available
		for word in synonyms:
			if len(word) > max_length:
				max_length = len(word)
				longest = word
	
	return longest

new_word = longest_synonym("what")
if new_word != "": # If a result is returned
	print(new_word)
