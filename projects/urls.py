from django.urls import path
from .views import ProjectDetailView, ProjectListCreateView, TagListCreateView, TagDetailView

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view()),
    path('project/<uuid:pk>/', ProjectDetailView.as_view()),
    path('tags/', TagListCreateView.as_view()),
    path('tag/<uuid:pk>/', TagDetailView.as_view()),
]