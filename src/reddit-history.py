import praw
from datetime import datetime

reddit = reddit = praw.Reddit('bot', user_agent='comment history bot (by /u/yourAccountName)')

collection = [
'yourAccountName',
'yourThrowawayAccount',
'yetAnotherThrowawayAccount'
]

for username in collection:
    for comment in reddit.redditor(username).comments.new(limit=None):
        id = comment.id.encode('utf-8').strip();
        date = datetime.fromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M')
        text = comment.body.encode('utf-8').strip()
        length = len(text)
        print(date + ', ' + id + ',' + str(length) + ', ' + text[0:15])