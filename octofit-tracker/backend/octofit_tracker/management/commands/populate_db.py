from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Workout, Activity, LeaderboardEntry
from django.utils import timezone
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db with sample data for testing'

    def handle(self, *args, **options):
        self.stdout.write('Populating database...')

        # Clear existing data
        LeaderboardEntry.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.filter(username__startswith='testuser').delete()

        # Create users
        users = []
        for i in range(1, 5):
            username = f'testuser{i}'
            user = User.objects.create_user(username=username, email=f'{username}@example.com', password='password')
            users.append(user)

        # Create teams
        t1 = Team.objects.create(name='Alpha Team')
        t1.members.set(users[:2])
        t2 = Team.objects.create(name='Beta Team')
        t2.members.set(users[2:])

        # Create workouts
        w1 = Workout.objects.create(name='Morning Run', difficulty='medium', suggested_duration_minutes=30)
        w2 = Workout.objects.create(name='Strength Training', difficulty='hard', suggested_duration_minutes=45)

        # Create activities
        activity_types = ['run', 'bike', 'swim', 'lift', 'yoga']
        for user in users:
            for _ in range(3):
                act_type = random.choice(activity_types)
                duration = random.uniform(20, 90)
                distance = random.uniform(1, 10) if act_type in ['run', 'bike', 'swim'] else None
                calories = int(duration * random.uniform(5, 10))
                act = Activity.objects.create(
                    user=user,
                    activity_type=act_type,
                    duration_minutes=duration,
                    distance_km=distance,
                    calories_burned=calories,
                    timestamp=timezone.now(),
                    workout=random.choice([w1, w2])
                )

        # Create leaderboard from activities
        for idx, user in enumerate(users, start=1):
            total_points = sum([int(a.duration_minutes) for a in user.activities.all()])
            LeaderboardEntry.objects.create(user=user, total_points=total_points, rank=idx)

        self.stdout.write(self.style.SUCCESS('Database populated.'))
