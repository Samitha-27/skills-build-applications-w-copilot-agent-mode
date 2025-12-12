from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
import os

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'workouts', views.WorkoutViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)

def api_root(request):
    from django.http import HttpResponse
    return HttpResponse(f"API root - {base_url}")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
