import praw
import time

print("Logging in...")
reddit = praw.Reddit(client_id = "tQ3AcC5Kro-9Rw", client_secret = "lcVvrLqY9PLGJRIKa0bLxml-Z1k", user_agent = "test_bot by /u/iamverysmart_bot", username = "iamverysmart_bot", password = "iamabotbleepbloop")
print(reddit.user.me())
print("Login successful.")

def run():
	print("Contacting subreddit...")
	subreddit = reddit.subreddit("test")
	print("Getting comments...")
	for submission in subreddit.hot(limit=2):
		comments = submission.comments
		for comment in comments:
			comment.reply("This is a test")
			print("Comment successful. Sleeping for 10 seconds...")
			time.sleep(10)

run()