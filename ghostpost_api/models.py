from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
  choices = (
    ('boast', 'Boast'),
    ('roast', 'Roast'),
  )
  choice_type = models.CharField(max_length=5, choices=choices, default='Boast')
  body = models.CharField(max_length=200)
  upVotes = models.IntegerField()
  downVotes = models.IntegerField()
  postDate = models.DateTimeField(default=timezone.now)
  totalVotes = models.IntegerField(default=0)

  def __str__(self):
    return self.body

  @property
  def total(self, *args, **kwargs):
    self.totalVotes = self.upVotes - self.downVotes
    super(Post, self).save(*args, **kwargs) 