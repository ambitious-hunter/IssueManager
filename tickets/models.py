from __future__ import unicode_literals

from django.db import models
# from accounts.models import User
from django.utils import timezone

BUG_STATUS = (
    ('To Do', 'To Do'),
    ('Doing', 'Doing'),
    ('Done', 'Done'),
)

BUG_TYPE = {
    ('BUG', 'Bug'),
    ('FTR', 'Feature'),
}


class Bug(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=BUG_STATUS, default='To Do')
    author = models.ForeignKey('accounts.User')
    views = models.IntegerField(default=0)
    issue_type = models.CharField(max_length=10, choices=BUG_TYPE, default='Bug')

    def publish(self):
        self.updated_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title

        # class Meta:
        #     db_table = 'bugs'

        # Create your models here.


# class Feature(Bug):
