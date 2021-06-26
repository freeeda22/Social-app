from django.contrib.auth import views
from . import views
from django.urls import path

urlpatterns = [
    # admin
    path('create-post/', views.CreatePost.as_view(),name="create-post"),
    path('story-status-count/<int:pk>/', views.StoryStatusCountAPIView.as_view(), name='story-status-count'), 

    #user
    path('list-story/<int:pk>/', views.StoryListAPIView.as_view(), name='list-story'),
    path('post-like-dislike/<int:pk>/<int:userid>/', views.StatusUpdateAPIView.as_view(), name='story-status'), 
    path('post-user-liked/<int:pk>/', views.UserListLikedPostAPIView.as_view(), name='user-list-liked-post'), 
]