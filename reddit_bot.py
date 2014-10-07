import ConfigParser
import time
import sys
import praw

USER_AGENT = '/u/YOUR_USERNAME_HERE'
SEARCH_FOR = 'PHRASE YOU ARE SEARCHING FOR'
MESSAGE = 'YOUR RESPONSE HERE'
SUBREDDIT = 'SUBREDDIT TO SEARCH'

SLEEPING = 100

r = praw.Reddit(user_agent = USER_AGENT)

config = ConfigParser.ConfigParser()
config.read('login.cfg')
username = config.get('auth', 'username')
password = config.get('auth', 'password')
r.login(username, password)

already_done = set()

super_comments = praw.helpers.comment_stream(r, SUBREDDIT, limit=400)

for comment in super_comments:
    sys.stdout.write('%s \n' % comment)
    if (comment.body).find(SEARCH_FOR) != -1 and comment.id not in already_done:
        try:
            comment.reply(MESSAGE)
        except: pass
        already_done.add(comment.id)
        time.sleep(SLEEPING)


        

