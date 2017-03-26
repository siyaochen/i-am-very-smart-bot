import time
from PyDictionary import PyDictionary

# Words that aren't replaced
excluded_words = ["your", "I", "they", "their", "we", "who", "them", "its", "our", "my", "those", "he", "us", "her", "something", "me", "yourself", "someone", "everything", "itself", "everyone", "themselves", "anyone", "him", "whose", "myself", "everybody", "ourselves", "himself", "somebody", "yours", "herself", "whoever", "you", "that", "it", "this", "what", "which", "these", "his", "she", "lot", "anything", "whatever", "nobody", "none", "mine", "anybody", "some", "there", "all", "where", "another", "same", "certain", "nothing", "self", "nowhere"]
# Append comment to cache if already processed (write to .txt file?)
cache = []
# Append word to word_cache if already replaced
word_cache = []

# Login
print("hi")
print("\nThis is the test client.")
print("I-am-very-smart bot 1.0 /u/iamverysmart_bot\n")

# Given a word, returns the longest synonym
def longest_synonym(word):
	dictionary = PyDictionary()
	synonyms = dictionary.synonym(word)
	longest = ""

	max_length = 0
	# If synonyms are available
	if synonyms is not None:
		for new_word in synonyms:
			if len(new_word) > max_length:
				max_length = len(new_word)
				longest = new_word
	
	return longest

# Replaces a word within a comment with another word
def replace(comment, old_word, new_word):
	if not new_word == old_word:
		# Check for capitalization in word
		if old_word[0].isupper():
			new_word = new_word.title()

		# Check for punctuation at the end of the word
		if old_word[len(old_word) - 1] == ".":
			new_word += "."
		elif old_word[len(old_word) - 1] == ",":
			new_word += ","
		elif old_word[len(old_word) - 1] == "!":
			new_word += "!"
		elif old_word[len(old_word) - 1] == "?":
			new_word += "?"
		elif old_word[len(old_word) - 1] == ":":
			new_word += ":"
		elif old_word[len(old_word) - 1] == ";":
			new_word += ";"
		elif old_word[len(old_word) - 1] == "...":
			new_word += "..."

	# Replace word in a list
	words = comment.split()
	for n in range(len(words)):
		if words[n] == old_word:
			words[n] = new_word
	
	# Need to fix line break issue
	# Reconstructs the text with a space between each element
	new_comment = ""
	for n in range(len(words)):
		new_comment += words[n]
		new_comment += " "

	return new_comment

# Run the bot
def run():
	print("Reading comment...\n")

	# Read comment from file
	comment_file = open("sample_comments/sample_comment_1.txt")
	text = comment_file.read()
	new_text = text

	print("Here is the old comment:")
	print(new_text + "\n")

	# Replace words
	for word in new_text.split():
		new_word = ""
		# If the word matches all the criteria
		if not word in excluded_words and not word in word_cache and len(word) >= 5:
			print("Here is the old word: " + word)
			# Find longest synonym
			new_word = longest_synonym(word)
			if len(new_word) <= len(word):
				new_word = word

			print("Here is the new word: " + new_word)
			# Replace all instances of word with synonym
			new_text = replace(new_text, word, new_word)	
			# Add word to word_cache
			word_cache.append(new_word)
	# Post comment
	print("Here is the processed comment:")
	print(new_text)

	# Write to file
	write_comment_file = open("sample_comments/sample_output_comment_1.txt", "w+")
	write_comment_file.write("Previous Comment:\n")
	write_comment_file.write(text)
	write_comment_file.write("\n\nProcessed Comment:\n")
	write_comment_file.write(new_text)
	write_comment_file.close

	# Add comment to cache
	cache.append("comment here")

# Main loop
again = True
while again:
	print("\nRunning program...")
	run()
	# Sleep for 10 seconds
	again = False
	str_again = input("Run again? ")
	if str_again is "yes":
		again = True

