import praw
import time
import PyDictionary

excluded_words = ["I", "that", "the", "they", ""]
# Append to cache if already processed (write to .txt file?)
cache = []

# Login
print("Attempting to login...")
r = praw.Reddit(user_agent = "I-am-very-smart bot 1.0 /u/iamverysmart_bot")
r.login()
print("Successfully logged in.")

# Given a word, returns the longest synonym
def longest_synonym(word):
	dictionary = PyDictionary()
	synonyms = dictionary.synonym(word)
	longest = ""

	max_length = 0
	# If synonyms are available
	if synonyms is not None:
		for word in synonyms:
			if len(word) > max_length:
				max_length = len(word)
				longest = word
	
	return longest

# Replaces a word within a comment with another word
def replace(comment, word):
	#Stuff here

# Run the bot
def run():
	subreddit = r.get_subreddit("test")
	comments = subreddit.get_comments(limit = 10)

	# Loop through comments, reply to some
	for comment in comments:
		if len(comment) > 30 and len(comment) < 200:
			new_comment = comment
			text = comment.body
			for word in text:
				# If the word matches the criteria
				if not (word[0].isupper() and word in excluded_words) and len(word) >= 5:
					new_word = longest_synonym(word)
				# Replace word with synonym
				new_commment = replace(new_comment, new_word)

while True:
	run()
	# Sleep for 10 seconds
	time.sleep(10)

