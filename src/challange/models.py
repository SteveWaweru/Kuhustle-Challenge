from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=45)

    def __unicode__(self):
        return self.title


class Bid(models.Model):
    job = models.ForeignKey(Job)
    price = models.DecimalField(max_digits=1000, decimal_places=2)

    def __unicode__(self):
        return str(self.price)


class User(models.Model):
    username = models.CharField(max_length=20)
    job = models.ForeignKey(Job)
    bids = models.ManyToManyField(Bid)

    def __unicode__(self):
        return self.username
