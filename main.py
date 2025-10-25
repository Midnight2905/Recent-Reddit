import praw

#self information
reddit = praw.Reddit(
    client_id = "YOUR ID",
    client_secret = "YOUR SECRET",
    user_agent = "ANY NAME"
)

#get a subreddit
subreddit = reddit.subreddit("SUBREDDIT NAME")

#gets the newest reddit stories
running = True

recent_post = ""
while running:
    for submission in subreddit.new(limit=1):
        #step 1) check if submission is empty
        #step 2) if the string is empty set it to the new recent post
        #step 3) if the new recent post != submission then 
        if(recent_post != submission.title):
            recent_post = submission.title
            print (submission.selftext)
            print(recent_post)
            print("\n\n")

