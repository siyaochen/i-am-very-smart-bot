import praw
import time

print("Logging in...")
reddit = praw.Reddit(client_id='tQ3AcC5Kro-9Rw', client_secret="lcVvrLqY9PLGJRIKa0bLxml-Z1k", user_agent='Test Bot by /u/iamverysmart_bot')
print("Login successful.")

def run():
	print("Contacting subreddit...")
	subreddit = reddit.subreddit("learnprogramming")
	print("Getting comments...")
	for submission in subreddit.hot(limit=10):
		comments = submission.comments
		for comment in comments:
			print(comment.body)

run()