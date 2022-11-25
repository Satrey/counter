from django.db import models


class Counter(models.Model):
    counter = models.IntegerField(blank=False, null=True)

    def __str__(self):
        return self.counter
