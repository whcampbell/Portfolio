from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Entry(models.Model) :
    title = models.CharField(max_length=128)
    body = models.TextField()
    post_time = models.DateTimeField(default=timezone.now)

    def __str__(self) :
        return self.title
    
    class Meta:
        ordering= ["-post_time"]

class Comment(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    post_time = models.DateTimeField(default=timezone.now)
    body = models.CharField(max_length=512)

    def __str__(self) :
        return self.user.username + "'s comment"

