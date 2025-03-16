from django.db import models


class Event(models.Model):
    name= models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=400)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='events', null=True)


    def __str__(self):
        return self.name
    


class Participant(models.Model):
    name= models.CharField(max_length=250)
    email = models.EmailField()
    events = models.ManyToManyField(Event, related_name="participants", blank=True)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.name


class Contact_Us(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name