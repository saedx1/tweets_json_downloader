# TweetsJSONDownloader
A script that takes a list of comma-separated `tweet_id`s and downloads their corresponding JSON objects.

Dependencies:
  - `click`
  - `tqdm`
  - `tweepy`

```
Usage: script.py [OPTIONS] CONSUMER_TOKEN CONSUMER_SECRET ACCESS_TOKEN
                 ACCESS_TOKEN_SECRET TWEET_IDS_CSV_FILE OUTPUT_JSON_FILE

Options:
  --wait_between_requests FLOAT
  --help                         Show this message and exit.
```
