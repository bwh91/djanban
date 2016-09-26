from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

#class Milestone(models.Model):
#    name = models.CharField(max_length=50)
#    description = models.TextField()
#    date_complete = models.DateField()
#    project = models.ForaignKey(Project)
#
#    def __str__(self):
#        return self.name

class Story(models.Model):
    name = models.CharField(max_length=50)
    assigned_to = models.ForeignKey(User, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    sprint = models.IntegerField(blank=True, null=True)
    project = models.ForeignKey(Project)
    complete_on = models.DateField(blank=True, null=True)

    TODO = "ToDo"
    DOING = "Doing"
    DONE = "Done"
    STATUS_CHOICE = (
        (TODO, 'ToDo'),
        (DOING, 'Doing'),
        (DONE, 'DONE'),
    )
    status = models.CharField(
        max_length=5,
        choices=STATUS_CHOICE,
        default=TODO,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Stories"
