import praw
import time
from PyDictionary import PyDictionary

# Words that aren't replaced
excluded_words = ["your", "I", "they", "their", "we", "who", "them", "its", "our", "my", "those", "he", "us", "her", "something", "me", "yourself", "someone", "everything", "itself", "everyone", "themselves", "anyone", "him", "whose", "myself", "everybody", "ourselves", "himself", "somebody", "yours", "herself", "whoever", "you", "that", "it", "this", "what", "which", "these", "his", "she", "lot", "anything", "whatever", "nobody", "none", "mine", "anybody", "some", "there", "all", "where", "another", "same", "certain", "nothing", "self", "nowhere"]

# Append word to word_cache if already replaced
word_cache = []

# Login
print("Attempting to login...")
reddit = praw.Reddit(client_id = "tQ3AcC5Kro-9Rw", client_secret = "lcVvrLqY9PLGJRIKa0bLxml-Z1k", user_agent = "test_bot by /u/iamverysmart_bot", username = "iamverysmart_bot", password = "iamabotbleepbloop")
print("Login successful.")

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
		elif old_word[0] == "\"":
			new_word = "\"" + new_word
		elif old_word[len(old_word) - 1] == "\"":
			new_word += "\""
			
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
	# Open file cache
	cache_file = open("cache.txt")
	cache = cache_file.read().split()

	# Get subreddit
	print("Attempting to contact subreddit...")
	subreddit = reddit.subreddit("iamverysmart")
	print("Getting comments...")

	# Get submission
	submission = next(x for x in subreddit.hot(limit = 10) if not x.stickied)

	comments = submission.comments
	# Loop through comments, reply to some
	for comment in comments:
		# Check to see if comment length matches
		if len(comment.body) > 30 and len(comment.body) < 400 and comment not in cache:
			# Add comment to cache
			cache.append(comment)
			changed = False
			print("Suitable comment found. Processing comment...")
			new_text = comment.body
			print("Here is the old comment:")
			print(comment.body)
			for word in new_text.split():
				new_word = ""
				# If the word matches all the criteria
				if word not in excluded_words and word not in word_cache and len(word) >= 5:
					# Find longest synonym
					new_word = longest_synonym(word)
					if len(new_word) <= len(word):
						new_word = word
					changed = True

					# Replace all instances of word with synonym
					new_text = replace(new_text, word, new_word)
					# Add word to word_cache
					word_cache.append(new_word)
			# Post comment
			if changed:
				print("Here is the processed comment:")
				print(new_text)
				print("Attempting to comment...")
				comment.reply('''I am a bot, *bleep*, *bloop*. I have attempted to calculate how someone from /r/iamverysmart would say your comment:  \n  ***  \n''' + new_text)


# Main loop
while True:
	print("Running program...")
	run()
	# Sleep for 10 seconds
	print("Sleeping for 10 seconds...")
	time.sleep(10)
