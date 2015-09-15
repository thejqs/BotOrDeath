from django.db import models

# Create your models here.


class IzzardTweet(models.Model):
    tweet = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tweet
