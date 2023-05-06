import tweepy
import time
import random
from plyer import notification
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from api_key import OPENAI_KEY
import openai

# Replace this with your OpenAI API key
openai.api_key = OPENAI_KEY
NEWS_LIST =  ['tier10k','News_Of_Alpha']
# Replace these with your own API credentials

API_KEY = "sYDNHT2T6XP3pyW7JRyiXvLnp"
API_SECRET = "YS6yBF95riDH2IaHnnAzCyQB3zN00lShEIPJql6ekvkML9zkTn"
ACCESS_TOKEN = "2414606610-rKc2WqS2uoXWen9HS14gcUrRSigSL3l30keMXNj"
ACCESS_SECRET = "hXoJK10NwQS9fsXMYaNSubCpHqZBwztF67Bi738Qzqmy7"

def authenticate(api_key, api_secret, access_token, access_secret):
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    return api

def get_tweets(api, user, count=10):
    tweets = api.user_timeline(screen_name=user, count=count, tweet_mode='extended')
    
    # for tweet in tweets:
    #     print(f"{tweet.user.screen_name}: {tweet.full_text}\n")
    return tweets

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )

def monitor_user_tweets(user_name, api, interval=60):
    for user in user_name:
        last_tweet_id = None

        while True:
            tweets = api.user_timeline(screen_name=user, since_id=last_tweet_id, tweet_mode='extended')
            
            if tweets:
                last_tweet_id = tweets[0].id
                for tweet in reversed(tweets):
                    print(f"{tweet.user.screen_name} at {tweet.created_at}: {tweet.full_text}\n")
                    send_notification(f"New tweet from {tweet.user.screen_name}", tweet.full_text)
        
    time.sleep(interval)

def get_list_id_by_name(api, screen_name, list_name):
    lists = api.get_lists(screen_name=screen_name)

    for list_item in lists:
        if list_item.name == list_name:
            return list_item.id

    return None

def get_list_members(api, list_id):
    members = tweepy.Cursor(api.get_list_members, list_id=list_id).items()

    usernames = []
    for member in members:
        usernames.append(member.screen_name)
        print(f"Username: {member.screen_name}")

    return usernames

def auto_like_quote(api, user_screen_name, interval=60, random=True,
                    min_interval=60, max_interval=120):
    last_tweet_id = None

    while True:
        tweets = api.user_timeline(screen_name=user_screen_name, since_id=last_tweet_id, tweet_mode='extended')
        
        if tweets:
            last_tweet_id = tweets[0].id
            for tweet in reversed(tweets):
                try:
                    # Like the tweet
                    api.create_favorite(tweet.id)
                    print(f"Liked tweet ID: {tweet.id}")
                except tweepy.TweepyException as e:
                                    print(f"Error while liking and quoting tweet ID: {tweet.id}. Error message: {e}")
                
                try:
                    # Quote the tweet
                    quote_text = f"{tweet.full_text} https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
                    api.update_status(status=quote_text)
                    print(f"Quoted tweet ID: {tweet.id}")
                except tweepy.TweepyException as e:
                    print(f"Error while liking and quoting tweet ID: {tweet.id}. Error message: {e}")

                # Sleep between actions to avoid hitting rate limits
                time.sleep(5)
        if random:
            interval = random.randint(min_interval, max_interval)
        time.sleep(interval)


def analyze_sentiment(text, tickerlist=None, analyzer='nltk'):
    crypto_ticker = tickerlist

    if analyzer == 'nltk':
        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(text)
        return sentiment_scores
    
    elif analyzer == 'openai':
        prompt = f"Please analyse the following tweet: \"{text}\":\
                first, extract any cryptocurrency token from the tweet,\
                second, analyze the market sentiment,\
                finally, give it a score from 0 to 100 as negative to positive,\
                output as following formnat 1.Crypto token: 2.Sentiment: 3.Score:"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()
    
import requests
from bs4 import BeautifulSoup

def get_coindesk_latest_headlines():
    url = "https://news.treeofalpha.com/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        latest_news_section = soup.find("section", class_="latest-news")
        articles = latest_news_section.find_all("div", class_="card")

        headlines_timestamps = []

        for article in articles:
            headline = article.find("h4", class_="card-title")
            timestamp = article.find("time")

            if headline and timestamp:
                headlines_timestamps.append((headline.text.strip(), timestamp["datetime"]))

        return headlines_timestamps
    else:
        print(f"Error: {response.status_code}")
        return None

def get_bybit_tickers():
    url = "https://api.bybit.com/v2/public/tickers"
    response = requests.get(url)
    
    if response.status_code == 200:
        tickers = response.json()["result"]
        ticker_list = []
        for ticker in tickers:
             ticker_list.append(ticker['symbol'])
        return ticker_list
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == '__main__':

    # scrape tweets from twitter
    api = authenticate(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    interval = 60
    username = 'TheCoinMonitor_'
    tweets = get_tweets(api, username)

    for tweet in tweets:
        sentiment = analyze_sentiment(tweet.full_text, analyzer='openai')
        print(f"{tweet.user.screen_name} at {tweet.created_at}: {tweet.full_text}\n")
        print(sentiment)
        print('------------------------------------------------')

    