from datetime import timedelta
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

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
    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    content = models.TextField()
    # likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    duration = models.IntegerField(default=30)  # D-day 지속 일수

    @property
    def d_day(self):
        days_remaining = (self.created_at + timedelta(days=self.duration)).date() - timezone.now().date()
        if days_remaining.days < 0:
            return "End"
        return f"D-{days_remaining.days}"