from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    CATEGORY_CHOICES = (
        ('MO', 'Morestudents'),
        ('CU', 'Curriculum'),
        ('PR', 'Professor'),
        ('ET', 'Etc'),
    )
    STATUS_CHOICES = (
        ('CU', 'Current'),
        ('EN', 'End'),
    )
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title