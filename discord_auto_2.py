import time 
import random 
import requests

tweet_dispatch= "https://discord.com/api/v9/channels/1090914294574616626/messages"


header = {
    'authorization': 'ODcyMDc0OTczMzQ1MzY2MDU2.GvotAr.q0YUUzW4hChI27h_jOusKBROfm6jbowjw39vLM'
}

def update_tweet_batch():
    """ Put used links to tobedelete.txt, update input_tweet.txt, get a new list of links.
    """
    input_file = open(input, "r")
    input_msgs = input_file.readlines()
    input_file.close()
    used_file = open(delete, "r")
    used_msgs = used_file.readlines()
    used_file.close()
    msgs = []
    with open(input, "w") as input_file:
        for msg in input_msgs:
            if msg not in used_msgs:
                input_file.write(msg)
                if "twitter" in msg:
                    msgs.append(msg)
    return msgs

def bot_post(msgs):
    """ Import list of tweet links to post
    """
    count = 0
    sent_msg = 0
    del_file = open(delete, "a")
    while len(msgs) > 0:
        toSend_msg = msgs[0]
        if "twitter" in toSend_msg and toSend_msg != sent_msg:
            # tweet count
            count += 1
            print("-------")
            print(count,"/",len(msgs))
            # send to cord
            payload = {
            'content': toSend_msg
            }
            r = requests.post(tweet_dispatch, data =payload, headers=header )
            print("post sent at ",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time())) )
            #dump to delete_tweets
            del_file.write(toSend_msg)
            del_file.flush()
            #remove from batch
            msgs.remove(toSend_msg)
            # reset
            sent_msg = toSend_msg
            #manual timer
            time.sleep(time_out + random_addTime*random.random())
        else:
            # remove disqualified tweets
            msgs.remove(toSend_msg)
            print("not a tweet link!")
    del_file.close()


def bot_post_test(msgs):
    """ Import list of tweet links to post
    """
    count = 0
    sent_msg = 0
    del_file = open(delete, "a")
    while len(msgs) > 0:
        toSend_msg = msgs[0]
        if "twitter" in toSend_msg and toSend_msg != sent_msg:
            # tweet count
            count += 1
            print("-------")
            print(count,"/",len(msgs))
            # send to cord
            payload = {
            'content': toSend_msg
            }
            # r = requests.post(tweet_dispatch, data =payload, headers=header )
            print("post sent at ",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time())) )
            #dump to delete_tweets
            del_file.write(toSend_msg)
            del_file.flush()
            #remove from batch
            msgs.remove(toSend_msg)
            # reset
            sent_msg = toSend_msg
            #manual timer
            # time.sleep(600 + 5*random.random())
        else:
            # remove disqualified tweets
            msgs.remove(toSend_msg)
            print("not a tweet link!")
    del_file.close()

time_out = 600 # seconds
random_addTime = 3 # seconds
real_run = True
if real_run:
    # real run
    input = "input_tweet.txt"
    delete = "delete_tweet.txt"
    state = True
    while state:
        msgs = update_tweet_batch()
        if len(msgs) >0:
            print("number of remaining tweets: ", len(msgs))
            bot_post(msgs)
        else:
            msgs = update_tweet_batch()
            if len(msgs) < 1:
                print("no more tweets in input file!!")
                state = False
else:
    # test run
    input = "test_input.txt"
    delete = "test_delete.txt"

    state = True
    while state:
        msgs = update_tweet_batch()
        if len(msgs) >0:
            print("number of remaining tweets: ", len(msgs))
            bot_post_test(msgs)
        else:
            msgs = update_tweet_batch()
            if len(msgs) < 1:
                print("no more tweets in input file!!")
                state = False



