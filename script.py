import tweepy
import time
import click
import json
from tqdm import tqdm


@click.command()
@click.argument("consumer_token")
@click.argument("consumer_secret")
@click.argument("access_token")
@click.argument("access_token_secret")
@click.argument(
    "tweet_ids_csv_file", type=click.Path(exists=True, file_okay=True, dir_okay=False)
)
@click.argument("output_json_file")
@click.option("--wait_between_requests", default=0.5, type=click.FLOAT)
def get_tweets(
    consumer_token,
    consumer_secret,
    access_token,
    access_token_secret,
    tweet_ids_csv_file,
    output_json_file,
    wait_between_requests,
):

    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    with open(tweet_ids_csv_file, "r") as reader:
        line = reader.readline()
        ids = line.split(",")

    tweets = []
    for i in tqdm(ids, unit="tweets"):
        try:
            tweets.append(api.get_status(i)._json)
        except tweepy.TweepError:
            pass
        time.sleep(wait_between_requests)

    with open(output_json_file, "w", encoding="utf-8") as f:
        json.dump(tweets, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    get_tweets()