from django.db import models

class Centre(models.Model):
    centre_name = models.CharField(max_length=250)
    centre_location = models.CharField(max_length=500)
    centre_topo = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        name = self.centre_name + ' (' + self.centre_location + ')'
        return name

class Climb(models.Model):
    climb_colour = models.CharField(max_length=250)
    climb_grade = models.CharField(max_length=2)

    def __str__(self):
        name = self.climb_colour + ' V' + self.climb_grade
        return name

class Climber(models.Model):
    climber_name = models.CharField(max_length=100)
    climber_age = models.IntegerField()

    def __str__(self):
        name = self.climber_name
        return name