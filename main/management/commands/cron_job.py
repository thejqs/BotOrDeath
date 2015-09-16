from django.core.management.base import BaseCommand
import os, sys

sys.path.append("../../..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import IzzardTweet


class Command(BaseCommand):

    def handle(self, *args, **options):
        help = "Makes a new tweet for BotOrDeath."
        # try:
        IzzardTweet.bot_or_death()
        # except Exception as e:
        #     print e
