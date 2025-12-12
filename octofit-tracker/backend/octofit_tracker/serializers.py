from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Activity, Team, Workout, LeaderboardEntry

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

    def get_id(self, obj):
        return str(obj.id)

class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = '__all__'

    def get_id(self, obj):
        return str(obj.id)

class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'

    def get_id(self, obj):
        return str(obj.id)

class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Workout
        fields = '__all__'

    def get_id(self, obj):
        return str(obj.id)

class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = LeaderboardEntry
        fields = '__all__'

    def get_id(self, obj):
        return str(obj.id)
