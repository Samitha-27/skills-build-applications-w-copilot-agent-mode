from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Workout, Activity, LeaderboardEntry

User = get_user_model()

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='batman', email='batman@dc.com', password='testpass')
        self.assertEqual(user.username, 'batman')
        self.assertEqual(user.email, 'batman@dc.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Justice League')
        self.assertEqual(team.name, 'Justice League')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Hero Training', difficulty='hard', suggested_duration_minutes=90)
        self.assertEqual(workout.name, 'Hero Training')
        self.assertEqual(workout.difficulty, 'hard')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='testpass')
        workout = Workout.objects.create(name='Amazon Training', difficulty='medium')
        activity = Activity.objects.create(user=user, activity_type='run', duration_minutes=60, workout=workout)
        self.assertEqual(activity.user.username, 'wonderwoman')
        self.assertEqual(activity.activity_type, 'run')

class LeaderboardEntryModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create_user(username='flash', email='flash@dc.com', password='testpass')
        entry = LeaderboardEntry.objects.create(user=user, total_points=100, rank=1)
        self.assertEqual(entry.user.username, 'flash')
        self.assertEqual(entry.total_points, 100)
        self.assertEqual(entry.rank, 1)
