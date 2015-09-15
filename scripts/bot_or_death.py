#!usr/bin/env python

import os, sys
import time
import tweepy

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from project.settings_local import auth_settings
from markov_izzard import BotOrDeath

auth = tweepy.OAuthHandler(auth_settings['consumer_key'], auth_settings['consumer_secret'])
auth.set_access_token(auth_settings['access_token_key'], auth_settings['access_token_secret'])
api = tweepy.API(auth)

or_death = BotOrDeath.read_eddie()

print type(or_death)
# api.update_status(or_death)
