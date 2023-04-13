from django.db import models

# Create your models here.


class Chat(models.Model):
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True)
    senderId = models.CharField(default='0', max_length=10)
    receiverId = models.CharField(default='0', max_length=10)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:20]


class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
