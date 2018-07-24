# reddit-history

Simple script to scrape reddit comment history.

1. `$ git clone https://github.com/mikechabot/reddit-history.git`
2. `$ pip install praw`
3. Rename `praw.default.ini` to `praw.ini`.
4. Add your client ID, client secret, username and password to `praw.ini`.
5. Update `reddit-history.py` with the usernames you'd like to scrape.
6. `$ python ./src/reddit-history.py > results.txt`
