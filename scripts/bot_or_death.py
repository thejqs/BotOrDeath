#!usr/bin/env python

import os, sys
import time
import tweepy

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from project.settings_local import auth_settings
from markov_izzard import BotOrDeath
from main.models import IzzardTweet


def bot_or_death():
    auth = tweepy.OAuthHandler(auth_settings['consumer_key'], auth_settings['consumer_secret'])
    auth.set_access_token(auth_settings['access_token_key'], auth_settings['access_token_secret'])
    api = tweepy.API(auth)

    or_death = BotOrDeath.read_eddie()

    tweet = IzzardTweet()
    tweet.tweet = or_death
    tweet.save()

    # print type(or_death)
    # print or_death

    api.update_status(status=or_death)

if __name__ == '__main__':
    bot_or_death()
