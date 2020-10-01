from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
  choices = models.BooleanField(choices=(
    (True, 'Boast'),
    (False, 'Roast'),
  ), default=True)
  body = models.CharField(max_length=200)
  upVotes = models.IntegerField()
  downVotes = models.IntegerField()
  postDate = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.body

  @property
  def total(self):
    return self.upVotes - self.downVotes