from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Team(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(User, related_name='teams', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Workout(models.Model):
    DIFFICULTY_CHOICES = [('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')]
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='easy')
    suggested_duration_minutes = models.PositiveIntegerField(default=30)

    def __str__(self):
        return self.name

class Activity(models.Model):
    ACTIVITY_TYPE_CHOICES = [
        ('run', 'Run'),
        ('bike', 'Bike'),
        ('swim', 'Swim'),
        ('lift', 'Lift'),
        ('yoga', 'Yoga'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=10, choices=ACTIVITY_TYPE_CHOICES)
    duration_minutes = models.FloatField(default=0.0)
    distance_km = models.FloatField(null=True, blank=True)
    calories_burned = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    workout = models.ForeignKey(Workout, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} @ {self.timestamp}"

class LeaderboardEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_points = models.IntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-total_points']

    def __str__(self):
        return f"{self.user.username} - {self.total_points}pts"
