from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Workout, Activity, LeaderboardEntry
from django.utils import timezone
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data (superheroes, Marvel/DC teams)'

    def handle(self, *args, **options):
        self.stdout.write('Populating database...')

        # Clear existing data
        LeaderboardEntry.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.filter(username__in=[
            'superman', 'batman', 'wonderwoman', 'flash',
            'ironman', 'spiderman', 'captainamerica', 'hulk'
        ]).delete()

        # Create superhero users
        marvel_heroes = [
            {'username': 'ironman', 'email': 'ironman@marvel.com'},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com'},
            {'username': 'hulk', 'email': 'hulk@marvel.com'},
        ]
        dc_heroes = [
            {'username': 'superman', 'email': 'superman@dc.com'},
            {'username': 'batman', 'email': 'batman@dc.com'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com'},
            {'username': 'flash', 'email': 'flash@dc.com'},
        ]
        users = []
        for hero in marvel_heroes + dc_heroes:
            user = User.objects.create_user(username=hero['username'], email=hero['email'], password='password')
            users.append(user)

        # Create teams Marvel and DC
        marvel_team = Team.objects.create(name='Team Marvel')
        marvel_team.members.set(users[:4])
        dc_team = Team.objects.create(name='Team DC')
        dc_team.members.set(users[4:])

        # Create workouts
        w1 = Workout.objects.create(name='Save the World', difficulty='hard', suggested_duration_minutes=60)
        w2 = Workout.objects.create(name='Secret Training', difficulty='medium', suggested_duration_minutes=45)

        # Create activities for each hero
        activity_types = ['run', 'bike', 'swim', 'lift', 'yoga']
        for user in users:
            for _ in range(3):
                act_type = random.choice(activity_types)
                duration = random.uniform(30, 120)
                distance = random.uniform(1, 20) if act_type in ['run', 'bike', 'swim'] else None
                calories = int(duration * random.uniform(8, 15))
                Activity.objects.create(
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

        self.stdout.write(self.style.SUCCESS('Populate the octofit_db database with test data'))

