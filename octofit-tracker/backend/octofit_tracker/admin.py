from django.contrib import admin
from .models import Team, Workout, Activity, LeaderboardEntry

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'suggested_duration_minutes')

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'duration_minutes', 'calories_burned', 'timestamp')
    list_filter = ('activity_type',)

@admin.register(LeaderboardEntry)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_points', 'rank')
