"""Markovify Finnegans Wake."""
import os
import time

import markovify
import twitter


def main():
    """All the things happen here."""
    # Load the text of Finnegans Wake
    with open("body.txt") as bolus:
        undigested = bolus.read()

    # Config stuff
    text_length = int(os.getenv("TEXT_LENGTH", "140"))
    twitter_vars = ["CONSUMER_KEY", "CONSUMER_SECRET",
                    "ACCESS_TOKEN_KEY", "ACCESS_TOKEN_SECRET"]
    twitter_api_settings = {x.lower(): os.getenv(x.upper())
                            for x in twitter_vars if os.getenv(x.upper())}
    # Prep markovify
    gizzard = markovify.Text(undigested)
    if twitter_api_settings:
        tweet_one(gizzard, twitter_vars, twitter_api_settings, text_length)
    else:
        print_ten(gizzard, text_length)


def print_ten(gizzard, text_length):
    """Print ten sentences from FW."""
    print("Standby! Ten lines of easy-to-digest JJ coming right up!\n\n")

    # Dramatic pause..
    time.sleep(1)
    finns = [gizzard.make_short_sentence(text_length) for x in range(10)]
    print("\n".join(finns))


def tweet_one(gizzard, twitter_vars, twitter_api_settings, text_length):
    """Tweet one if all settings are in place."""
    tweet_miss = [x for x in twitter_vars
                  if twitter_api_settings[x.lower()] is None]
    if tweet_miss:
        print("Missing the following vars necessary for tweeting: "
              "{}".format(", ".join(tweet_miss)))
        return
    api = twitter.Api(**twitter_api_settings)
    api.PostUpdate(gizzard.make_short_sentence(text_length))


if __name__ == "__main__":
    main()
