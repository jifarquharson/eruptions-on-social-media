import os
import json
import datetime as dt
import time
import tweepy
from tweepy import OAuthHandler

"""
X (Twitter) data mining script

This script retrieves tweets containing specific search phrases over a given timeframe.
It requires access to the Twitter API, which, as of March 2025, is no longer publicly available.
The script was used for data collection between 25 August 2019 and 12 June 2023.

To run:
    1. Register a Twitter API application (if access is restored).
    2. Obtain and enter authentication credentials below.
    3. Execute the script: `python [filename].py`
"""

# Twitter API Credentials (Replace with actual credentials)
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""

def load_api():
    """Authenticate and return a Tweepy API instance."""
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def tweet_search(api, query, max_tweets, max_id, since_id):
    """Search for tweets matching the given query parameters."""
    searched_tweets = []
    while len(searched_tweets) < max_tweets:
        try:
            new_tweets = api.search(
                q=query, count=max_tweets - len(searched_tweets),
                since_id=since_id, max_id=max_id - 1
            )
            if not new_tweets:
                print("No more tweets found.")
                break
            searched_tweets.extend(new_tweets)
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            print(f"Error: {e}. Waiting 15 minutes before retrying...")
            time.sleep(15 * 60)
            break
    return searched_tweets, max_id

def get_tweet_id(api, days_ago=9, query="a"):
    """Retrieve the tweet ID from a given number of days ago."""
    td = dt.datetime.now() - dt.timedelta(days=days_ago)
    tweet_date = td.strftime("%Y-%m-%d")
    tweet = api.search(q=query, count=1, until=tweet_date)
    return tweet[0].id if tweet else None

def write_tweets(tweets, filename):
    """Append collected tweets to a file in JSON format."""
    with open(filename, 'a') as f:
        for tweet in tweets:
            json.dump(tweet._json, f)
            f.write('\n')

def main():
    """Main function for executing the Twitter search script."""
    search_phrases = [] # list of search terms should go here (e.g. ["volcanic eruption", "eldgos", "화산 분출"])
    time_limit = 1.5  # Runtime limit in hours
    max_tweets = 100  # Tweets per search
    min_days_old, max_days_old = 1, 2  # Search timeframe
    
    api = load_api()
    start_time = dt.datetime.now()
    end_time = start_time + dt.timedelta(hours=time_limit)
    
    for search_phrase in search_phrases:
        print(f"Searching for: {search_phrase}")
        folder = f"data/{search_phrase.replace(' ', '_')}"
        os.makedirs(folder, exist_ok=True)
        json_file = f"{folder}/{search_phrase.replace(' ', '_')}_{dt.datetime.now().strftime('%Y-%m-%d')}.json"
        
        since_id = get_tweet_id(api, days_ago=max_days_old - 1) or 0
        max_id = get_tweet_id(api, days_ago=min_days_old - 1) or -1
        
        while dt.datetime.now() < end_time:
            tweets, max_id = tweet_search(api, search_phrase, max_tweets, max_id, since_id)
            write_tweets(tweets, json_file)
            if not tweets:
                break
        
        print(f"Search completed for: {search_phrase}")

if __name__ == "__main__":
    main()
