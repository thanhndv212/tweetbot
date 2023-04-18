import time 
import random 

count = 0

import requests

tweet_dispatch= "https://discord.com/api/v9/channels/1090914294574616626/messages"


header = {
    'authorization': 'ODcyMDc0OTczMzQ1MzY2MDU2.GvotAr.q0YUUzW4hChI27h_jOusKBROfm6jbowjw39vLM'
}
input_file = open("input_tweet.txt", "r")
input_msgs = input_file.readlines()
input_file.close()
used_file = open("delete_tweet.txt", "r")
used_msgs = used_file.readlines()
used_file.close()
msgs = []
with open('input_tweet.txt', "w") as input_file:
    for msg in input_msgs:
        if msg not in used_msgs:
            input_file.write(msg)
            msgs.append(msg)
# del_file = open("delete_tweet.txt", "a")

# for msg in msgs:
#        #discord
#     if "twitter" in msg:
#         count += 1
#         print("-------")
#         print(count)
#         payload = {
#         'content': msg
#         }
#         r = requests.post(tweet_dispatch, data =payload, headers=header )
#         print("post sent")
#         del_file.write(msg+ '\n')
#         del_file.flush()
#         time.sleep(600 + 30*random.random())
        
#     else:
#         print("not a tweet")