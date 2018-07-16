import datetime

from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


class Poll(models.Model):
    question = models.CharField(max_length=200)

    def __str__(self):              # Python 3: def __unicode__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):              # Python 3: def __unicode__(self):
        return self.choice_text


class Document(models.Model):
    title = models.CharField(max_length=80)
    # author = ?
    pub_date = models.DateTimeField('publish on')

    class Meta:
        abstract = True


class HowTo(Document):
    intro = models.CharField(max_length=500)
    tags = TaggableManager()

    def __str__(self):
        return '(title:"' + self.title + '"), (' + 'intro:"' + self.intro + '")'


class Step(models.Model):
    how_to = models.ForeignKey(HowTo, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    markdown_content = models.CharField(max_length=5000) # chang the length


# class TheoreticalArticle(models.Model):
#     pass
