from django.urls import path
from .views import TutorialDetailView, TutorialListView

urlpatterns = [
    path('tutorials/', TutorialListView.as_view()),
    path('tutorial/<uuid:pk>/', TutorialDetailView.as_view()),
]