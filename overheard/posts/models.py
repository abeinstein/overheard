from django.db import models
from jsonfield import JSONField

# Create your models here.
class Post(models.Model):
    ''' Represents on Overheard Post '''
    facebook_id = models.CharField(max_length=100, primary_key=True)
    permalink = models.URLField(blank=True, null=True, max_length=1000)
    body = models.TextField(blank=True, null=True)
    num_likes = models.PositiveIntegerField(blank=True, null=True)
    num_comments = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    poster = models.CharField(max_length=200)
    poster_id = models.CharField(max_length=100)

    has_picture = models.BooleanField(default=False)
    picture_url = models.URLField(blank=True, null=True, max_length=1000)

    # Stores the raw data
    # Only stores data for posts >1 week old
    raw_data = JSONField(blank=True, null=True)

    def __str__(self):
        return self.body

    def __unicode__(self):
        return unicode(self.body)


