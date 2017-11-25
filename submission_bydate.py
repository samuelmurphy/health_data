import praw
import unicodecsv as csv
import os
import sys
import time 
#from datetime import datetime, date, time,  timedelta
import datetime
import pprint

#        "ID",
  #      "Parent ID",

def insert_csv_header():
    #HEADER
    oout = [
        "Result Row",
        "Source Page URL",
        "Subreddit",
         "Post Title",
        "username",
        "date", 
        "time",
        "flare",
        "score",
        "Comment text"
    ]
    #print(oout)
    writer.writerow(oout)


def write_post_entries(reddit, submission):
#    print ("IN  write_post_entries ")
    title = submission.title
    try:
        selftext = submission.selftext
    except:
        selftext = "n/a"
    try:
        username = submission.author.name
    except:
        username = "n/a"
        
    oout = [
        "0",
        submission.url,
         submission.subreddit_name_prefixed,
         title,
        username,
        time.strftime('%Y-%m-%d', time.localtime(submission.created)),
        time.strftime('%H:%M:%S', time.localtime(submission.created)),
        submission.author_flair_text,
        submission.score,
        selftext
       ]
    writer.writerow(oout)

def reddit_thread(reddit, submission):
#    print("in reddit_thread")
    result_row = 0
    for cur_comment in submission.comments.list():
        try:
            name  = cur_comment.author.name
        except:
            name = "n/a"

        #DEBUG
  #      print ("=============================================")
#        print(name)
        #print ( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(cur_comment.created))  )
       # print("FLARE: " , cur_comment.author_flair_text)
        #print(cur_comment.score)
        #print(cur_comment.body)
        #print(cur_comment.submission.url)
        #print (cur_comment.subreddit)
        #print("    ")

        try:
            subreddit =   cur_comment.subreddit
        except:
            subreddit = ""
        try:
            day  =  time.strftime('%Y-%m-%d', time.localtime(cur_comment.created))
            time_formated   =  time.strftime('%H:%M:%S', time.localtime(cur_comment.created))
        except:
            day = ""
            time_formated = ""
        try:
            flare =  cur_comment.author_flair_text
        except:
            flare = ""
        try:
            score = cur_comment.score
        except:
            score = ""
        try:
            body = cur_comment.body
        except:
            body = ""
        result_row = result_row + 1
        oout = [
            result_row,
            cur_comment.submission.url,
            subreddit,
            "",  # title 
            name,
            day,
            time_formated,
            flare,
            score,
            # replace did not help
            #cur_comment.body.replace('\t', '<TAB>').replace('\r', ' --- ').replace('\n', ' --- ')
            body
        ]

        writer.writerow(oout )

#BEGIN PROGRAM
#ofile  = open('ttest.csv', "w", encoding='utf-8')
ofile  = open('ttest.csv', "wb")
#writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

insert_csv_header()

reddit = praw.Reddit(client_id='f67MPgz2UTcJuQ',
                     client_secret='bVuLjE9NV04gN2j2F2MKIga7mw8',
                     redirect_uri='http://www.samtheknife.com',
                     user_agent='/reddit/about_sams_scraper.html')


#subreddit = reddit.subreddit('ChronicPain')
print("begin")
submission_run_count = 0

# for submission in subreddit.new(limit=None):
#     submission.comments.replace_more(limit=0)
#     submission_run_count  += 1
#     if not submission_run_count % 100:
#         print ("subreddits read: {}".format(submission_run_count ))
#     write_post_entries(reddit, submission)
#    reddit_thread(reddit, submission)


curr_day  = datetime.datetime.combine(datetime.date.today(),  datetime.time.min)
#curr_day  = datetime.datetime.fromtimestamp(1498845107)
prev_day  =  curr_day  -  datetime.timedelta(days=1)

for i in range(313):
    cur = curr_day.timestamp()
    prev = time.mktime(prev_day.timetuple())
    for submission in reddit.subreddit('ChronicPain').submissions(prev, cur):
        
        write_post_entries(reddit, submission)
        reddit_thread(reddit, submission)
    
        print(submission.created_utc)
        print(submission.url)
        print()
        curr_day = prev_day
        prev_day = prev_day  -  datetime.timedelta(days=1)
    print("------------------------------------------------------------------------ {} -------------------".format(i))


print()
print("total threads: {} ".format(submission_run_count))
print("end run")
ofile.close()


         
