from django.core.management.base import BaseCommand
import os
from scripts.bot_or_death import bot_or_death


class Command(BaseCommand):

    def handle(self, *args, **options):
        help = "Makes a new tweet for BotOrDeath."
        try:
            bot_or_death()
        except:
            raise CommandError("Could not make a tweet. Boo.")


# /sites/virtualenvs/izzard/bin/python izzard/scripts/bot_or_death.py

# 7 10,15 * * * /sites/virtualenvs/izzard/bin/python /sites/projects/izzard/manage.py handle