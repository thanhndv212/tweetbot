import tweepy
import time 
import random 

# setup API main acc

api_key = "PJfF0Adam3RuXr6PuGIFD0zpl"
api_key_secret = "xObe3tUAH1ZZrW6EINdDIexBhPuJAZj2asQCpw7CQXRyrDjcYn"
access_token = "2414606610-jhEfIj2lKBj51jYGvSi07HYCovtTmZp8gJwnLwn"
access_token_secret = "SeqHK1tXaKHnVDLD3RQ2otSe8Uz3rJwywFADb6vf9aIlg"
bearer_token = "AAAAAAAAAAAAAAAAAAAAANW4mgEAAAAAPk%2BNVeQctlDXbt3jogjx2rNj1X8%3Do1yqQ1yMdwx4q46pZ5cFVwDOxF4BmJTjufIcKkmjWp5V7l6pmE"
client_id = "MGdCbTBzaTJlMVpDOGN4TDJPV2Y6MTpjaQ"
client_scrt = "VM7QKrhaCKxJFjb3e28qTTd0i_Pqoz77Ot6pxqhqXNyIE5XONS"
client = tweepy.Client(consumer_key=api_key, consumer_secret=api_key_secret,
                       access_token=access_token, access_token_secret=access_token_secret, wait_on_rate_limit=True)
auth_url = "https://twitter.com/i/oauth2/authorize"
token_url = "https://api.twitter.com/2/oauth2/token"
redirect_uri = "https://twitter.com"
# bot
msgs = []
random_text = ["Arbswap is the best DEX onn Arbitrum Nova!!!","To the moon","Get innn! Quick!", "Brilliant exchange!!", "Attention!! This is going to be massive.",
               "we all gonna make it", "join us!! still enough time", "plenty of opportunities, still there's a chance" , "brilliant minds, amazing teanm, absolutely great"]
hashtag = " #S1Hodler #DEX #airdrop $ARB #ArbEgg $ARBS #NFT #Arbsian #ArbswapAirdrop #Arbswap #Arbitrum @ArbswapOfficial "
count = 0

# oauth v1 user handler
client = tweepy.Client(consumer_key=api_key, consumer_secret=api_key_secret,
                access_token=access_token, access_token_secret=access_token_secret,
                 wait_on_rate_limit=True)


# # oauth v2 user handler
# import re
# import base64
# import os
# import hashlib
# from requests_oauthlib import OAuth2Session
# scopes = ["tweet.read", "users.read", "tweet.write", "offline.access"]

# code_verifier = base64.urlsafe_b64encode(os.urandom(30)).decode("utf-8")
# code_verifier = re.sub("[^a-zA-Z0-9]+", "", code_verifier)

# code_challenge = hashlib.sha256(code_verifier.encode("utf-8")).digest()
# code_challenge = base64.urlsafe_b64encode(code_challenge).decode("utf-8")
# code_challenge = code_challenge.replace("=", "")

# # twitter = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scopes)
# oauth2_user_handler = tweepy.OAuth2UserHandler(
#     client_id=client_id,
#     redirect_uri=redirect_uri,
#     scope=scopes,
#     # Client Secret is only necessary if using a confidential client
#     client_secret=client_scrt
# )

# print(oauth2_user_handler.get_authorization_url())

# authorization_response = input("--> ")

# access_token = oauth2_user_handler.fetch_token(
#     authorization_response
# )
# client = tweepy.Client(access_token["access_token"])


# response = client.create_tweet(
#     text="This Tweet was Tweeted using Tweepy and Twitter API v2!",
#     user_auth=False
# )
# print(f"https://twitter.com/user/status/{response.data['id']}")


with open('input_tweet.txt', "a") as file:
    while count<100:
        count += 1
        msg_text = random.choice(random_text) + hashtag + f"{random.randint(0,1000000)}"
        response = client.create_tweet(text=msg_text)
        # print("post created")
        msg = f"https://twitter.com/user/status/{response.data['id']}"
        # print(msg)
        file.write(msg+ '\n')
        file.flush()
        msgs.append(msg)
        # time.sleep(60)

    #discord
    # payload = {
    # 'content': msg
    # }
    # r = requests.post(tweet_dispatch, data =payload, headers=header )
    # print("post sent")
    # # sleep_delete = random.randint(60,100)
    # # time.sleep(sleep_delete)
    # # client.delete_tweet(id=response.data['id'])
    # # print("post deleted")
    # # time.sleep(300-sleep_delete)
    # time.sleep(random.randint(300,305))