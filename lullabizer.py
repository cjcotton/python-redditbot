# Don't use this for harassing people.
# It's a skeleton for responding to people
# whenever they make a post.
# You should probably refine it so that
# it's only if they respond to you, on a specific post, etc.
# Don't just post auto-generated responses
# on people's comments.

import praw
import time
import random
from config_bot import *

# Setting up the User Agent, because of the following;
# https://github.com/reddit/reddit/wiki/API
user_agent = ("Lullabies 0.1")
r = praw.Reddit(user_agent=user_agent)

# Login, reads from your creds.py
r.login(REDDIT_USERNAME, REDDIT_PASS)

# Initially, we just put their most recent comment in a file
# called previous.txt.
user = r.get_redditor('')
for comment in user.get_comments(limit=1):
    f = open( 'previous.txt', 'w' )
    f.write( repr(comment.body) )
    f.close()

# Now that we have their most recent comment tucked
# away, we can monitor every time that changes
# in comparison to the comment we wrote to the file.
# If it doesn't change, we just print 'No Change', but
# if it does change, we read in one line from our
# Lullabies.txt file, and then update the previous.txt file.
# After each of these, we sleep for 30 seconds.
while True:
    for comment in user.get_comments(limit=1):
        if comment.body in open('previous.txt').read():
            print "No Change"
            time.sleep(30)
        else:
            f = open('lullabies.txt')
            rFoxPhrase = random.choice(open('lullabies.txt').readlines())
            comment.reply(rFoxPhrase)
            f = open( 'previous.txt', 'w' )
            f.write( repr(comment.body) )
            f.close()
            time.sleep(30)
