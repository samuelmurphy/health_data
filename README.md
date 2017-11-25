# health_data

this is a working area for a project scraping data for a pain study at rutgers 

The data delivered was with a working file called "working_scrape.py" which had all parameters hard codeded as it was a work in progress until the final run. It's included as informational if needed but unlikely to  be useable except by me or another programmer.

A parameterized version called "health_scraper.py" could be more useful, details below. 

There seem to be some constraints on direct reddit access one transaction a second (or 600 each 10 minute interval). Also a retrieval limit of 1000 'items' 



The primary scrape code used the reddit api via a python wrapper "praw".


notes
https://github.com/praw-dev
https://github.com/pushshift/api
https://api.pushshift.io/reddit/submission/comment_ids/74p935
Docs:  https://praw.readthedocs.io/en/latest/


{
data: [
"do0l6mm",




https://github.com/voussoir/reddit/tree/master/Prawtimestamps
https://www.reddit.com/r/redditdev/comments/763poa/get_all_comments_from_a_subreddit/

pushshift.io

Pushshift is an interesting project that turned up, it's oriented to some research but seems to be a personal project but contains a lot of data including deleted comments. It's a scrape of all reddit in almost realtime, although there seem to be some processing lags. Not super documented I'm still investigating.


Docs:
https://pushshift.io/
https://github.com/pushshift/api

Info:
https://www.reddit.com/r/redditdev/
https://www.reddit.com/r/pushshift/
