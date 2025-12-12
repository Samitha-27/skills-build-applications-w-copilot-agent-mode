from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .models import Activity, Team, Workout, LeaderboardEntry
from .serializers import UserSerializer, ActivitySerializer, TeamSerializer, WorkoutSerializer, LeaderboardSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = LeaderboardEntry.objects.all()
    serializer_class = LeaderboardSerializer
