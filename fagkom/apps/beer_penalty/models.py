from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class AlkoEntry(models.Model):
    user = models.ForeignKey(User)
    beer_amount = models.IntegerField()
    wine_amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    justification = models.CharField(max_length=100)

    WINE_TO_BEER_RELATIONSHIP = 3

    def __unicode__(self):
        return "{date} {user}: {justification}".format(
            date=self.date,
            user=self.user,
            justification=self.justification,
        )

    def get_total_score(self):
        return (self.beer_amount * WINE_TO_BEER_RELATIONSHIP) + self.wine_amount

admin.site.register(AlkoEntry)
