from django.db import models

class Counter(models.Model):
    counter = models.IntegerField(blank=False, null=True, default=0)

    def __str__(self):
        return self.counter
