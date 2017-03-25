import praw
import time
import PyDictionary

# Words that aren't replaced
excluded_words = ["your", "I", "they", "their", "we", "who", "them", "its", "our", "my", "those", "he", "us", "her", "something", "me", "yourself", "someone", "everything", "itself", "everyone", "themselves", "anyone", "him", "whose", "myself", "everybody", "ourselves", "himself", "somebody", "yours", "herself", "whoever", "you", "that", "it", "this", "what", "which", "these", "his", "she", "lot", "anything", "whatever", "nobody", "none", "mine", "anybody", "some", "there", "all", "where", "another", "same", "certain", "nothing", "self", "nowhere"]
# Append comment to cache if already processed (write to .txt file?)
cache = []
# Append word to word_cache if already replaced
word_cache = []

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
		# Check to see if comment length matches
		if len(comment) > 30 and len(comment) < 200:
			new_comment = comment
			text = comment.body
			for word in text:
				new_word = ""
				# If the word matches all the criteria
				if not word[0].isupper() and not word in excluded_words and len(word) >= 5:
					new_word = longest_synonym(word)
					# Replace word with synonym
					new_commment = replace(new_comment, new_word)

# Main loop
while True:
	run()
	# Sleep for 10 seconds
	time.sleep(10)

