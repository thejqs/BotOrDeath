import os, sys
from django.db import models
from django.conf import settings
import tweepy
from project.settings_local import auth_settings
from random import choice
# import subprocess

# Create your models here.


class IzzardTweet(models.Model):
    tweet = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tweet

    @staticmethod
    def read_eddie():
        # print "read_eddie is starting"
        with open('/sites/projects/izzard/main/izzard.txt', 'r') as text_file:
            chain_dict = IzzardTweet.word_chains(text_file)
            random_text = IzzardTweet.make_random(chain_dict)

            return random_text

    @staticmethod
    def word_chains(source_text):
        content_list = source_text.read().split()

        izzard_dict = {}

        for i in range(len(content_list) - 2):
            izzard_key = (content_list[i], content_list[i + 1])
            next_word = content_list[i + 2]

            if izzard_key not in izzard_dict:
                izzard_dict[izzard_key] = []

            izzard_dict[izzard_key].append(next_word)

        return izzard_dict

    @staticmethod
    def make_random(chains):
        sentence = ''
        words = []
        random_key = choice(chains.keys())
        words.append(random_key[0])
        words.append(random_key[1])

        while random_key in chains:
            following_word = choice(chains[random_key])

            words.append(following_word)

            random_key = (random_key[1], following_word)

        # words_string = " ".join(words)

        for word in words:
            if len(word) + len(sentence) < 139:
                if sentence == '':
                    word = word.capitalize() + ' '
                    sentence += word
                else:
                    word = word + ' '
                    sentence += word

                if len(sentence) >= 130 and len(word) < 4:
                    break

                if len(sentence) >= 130 and ('. ' in word or '? ' in word):
                    break

        # subprocess.Popen(['say', sentence])
        return sentence

        # return words_string

    @staticmethod
    def bot_or_death():
        # import os, sys

        auth = tweepy.OAuthHandler(auth_settings['consumer_key'], auth_settings['consumer_secret'])
        auth.set_access_token(auth_settings['access_token_key'], auth_settings['access_token_secret'])
        api = tweepy.API(auth)

        # print "bot_or_death has authenticated"
        or_death = IzzardTweet.read_eddie()

        tweet = IzzardTweet()
        tweet.tweet = or_death
        tweet.save()

        api.update_status(status=or_death)
        print or_death
        print "\n\tThis tweet was %s characters long" % or_death
