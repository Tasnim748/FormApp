from django.db import models

# Create your models here.
class Sector(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Input(models.Model):
    username = models.CharField(max_length=100)
    sectors = models.ManyToManyField(Sector, related_name='sectors', blank=True)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username + "_" +  str(self.last_update)

    @property
    def date(self):
        return self.last_update.day

    @property
    def month(self):
        return self.last_update.month

    @property
    def year(self):
        return self.last_update.year

    # @property
    # def time(self):
    #     return self.last_update.get_time
    

